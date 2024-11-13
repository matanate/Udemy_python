from bs4 import BeautifulSoup
import requests

response = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
movie_title_tags = soup.select("h3.title")
year_tags = soup.select("strong")
for index, (tag_m, tag_y) in enumerate(zip(movie_title_tags, year_tags)):
    with open("movies.txt", "a", encoding="UTF-8") as f:
        f.write(f"{index+1}) {' '.join(tag_m.text.split(' ')[1:])}, {tag_y.text}\n")
