from flask import Flask, render_template
from post import Post
import random

app = Flask(__name__)

posts = Post()


@app.route("/")
def home():
    return render_template("index.html", all_posts=posts.all_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<post_id>")
def post(post_id):
    posts.get_post(post_id)
    return render_template(
        "post.html",
        title=posts.title,
        subtitle=posts.subtitle,
        body=posts.body,
        author=posts.author,
        date=posts.date,
        image_url=posts.image_url,
        image_alt=posts.image_alt,
    )


if __name__ == "__main__":
    app.run(debug=True)
