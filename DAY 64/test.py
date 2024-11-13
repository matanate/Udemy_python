import requests

movie_title = "The Witcher: Blood Origin"
url = f"https://api.themoviedb.org/3/search/movie?query={movie_title}&include_adult=false&language=en-US&page=1"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmM2JjZjZjODAxYmVkN2MxZmI3ZjFhYWUzMjA5YTA0NSIsInN1YiI6IjY1NjFlNzZkMDI4ZjE0MDBlMTMwMGE1MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.1D_YHIkN3RN9MsmKV91ugao9VfkWuBWhVIB1bvgIL6E",
}

response = requests.get(url, headers=headers).json()["results"]

for i in response:
    print(f"{i}")
