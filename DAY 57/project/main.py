from flask import Flask, render_template
from post import Post

app = Flask(__name__)

posts = Post()


@app.route("/")
def home():
    return render_template("index.html", all_posts=posts.all_posts)


@app.route("/post/<blog_id>")
def post(blog_id):
    posts.get_post(blog_id)
    return render_template(
        "post.html", title=posts.title, subtitle=posts.subtitle, body=posts.body
    )


if __name__ == "__main__":
    app.run(debug=True)
