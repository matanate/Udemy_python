import requests


class Post:
    def __init__(self):
        self.title = ""
        self.subtitle = ""
        self.body = ""
        self.response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
        self.all_posts = self.response.json()

    def get_post(self, post_id):
        for post in self.all_posts:
            if int(post["id"]) == int(post_id):
                self.title = post["title"]
                self.subtitle = post["subtitle"]
                self.body = post["body"]
