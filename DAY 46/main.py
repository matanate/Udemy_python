from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        show_dialog=True,
        cache_path="token.txt",
        username="Matanate",
    )
)
user_id = spotify.current_user()["id"]

input_date = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: "
)
response = requests.get(f"https://www.billboard.com/charts/hot-100/{input_date}")
soup = BeautifulSoup(response.text, "html.parser")
songs_tags = soup.select("li h3#title-of-a-story")
artist_tags = soup.select("li.o-chart-results-list__item span.c-label.a-no-trucate")
playlist_id = spotify.user_playlist_create(
    user=user_id,
    name=f"{input_date} Billboard 100",
    public=False,
    description=f"{input_date} Billboard 100",
)["id"]
uris = []
for tag_s, tag_a in zip(songs_tags, artist_tags):
    song = tag_s.text
    song = " ".join(song.split())
    artist = tag_a.text
    artist = " ".join(artist.split())
    try:
        request = spotify.search(type="track", q=f"{song} - {artist}")
        track_uri = str(request["tracks"]["items"][0]["uri"])
        uris.append(track_uri)
    except:
        print(f"The song: {song} - {artist}, does not exist on spotify.\nSkipped")


spotify.playlist_add_items(playlist_id, uris, None)
