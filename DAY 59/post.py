import requests


class Post:
    def __init__(self):
        self.title = ""
        self.subtitle = ""
        self.body = ""
        self.date = ""
        self.author = ""
        self.image_url = ""
        self.image_alt = ""
        self.response = requests.get("https://api.npoint.io/eb6cd8a5d783f501ee7d")
        self.all_posts = self.response.json()

    def get_post(self, post_id):
        for post in self.all_posts:
            if int(post["id"]) == int(post_id):
                self.title = post["title"]
                self.subtitle = post["subtitle"]
                self.body = post["body"]
                self.date = post["date"]
                self.author = post["author"]
                self.image_url = post["image_url"]
                self.image_alt = post["image_alt"]
