from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
storylinks_tags = soup.select("span.titleline a[rel = 'noreferrer']")
scores_tags = soup.select("span span.score")
dict = {}
for tag_t, tag_s in zip(storylinks_tags, scores_tags):
    dict[tag_t.text] = {
        "score": int(tag_s.text.split(" ")[0]),
        "link": tag_t.get("href"),
    }

max_key = max(dict, key=lambda key: dict[key]["score"])
print(
    f"{max_key} has the highest score of {dict[max_key]['score']}: {dict[max_key]['link']}"
)
