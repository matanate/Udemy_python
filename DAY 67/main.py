from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
import requests

app = Flask(__name__)
ckeditor = CKEditor(app)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
bootstrap = Bootstrap5(app)

# CONNECT TO DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
db = SQLAlchemy()
db.init_app(app)


# New Blog Form Definition
class NewBlogForm(FlaskForm):
    title = StringField(label="The blog post title", validators=[DataRequired()])
    subtitles = StringField(label="The subtitle", validators=[DataRequired()])
    author = StringField(label="The author's name", validators=[DataRequired()])
    bg_img_url = StringField(
        label="A URL for the background image", validators=[DataRequired()]
    )
    body = CKEditorField(
        label="The body (the main content) of the post", validators=[DataRequired()]
    )
    submit = SubmitField(label="Submit")


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def get_all_posts():
    posts = list(db.session.execute(db.select(BlogPost)).scalars())
    return render_template("index.html", all_posts=posts)


# TODO: Add a route so that you can click on individual posts.
@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = db.session.get(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route("/new-post", methods=["POST", "GET"])
def add_new_post():
    post_form = NewBlogForm()
    if post_form.validate_on_submit():
        post = BlogPost(
            title=post_form.title.data,
            subtitle=post_form.subtitles.data,
            author=post_form.author.data,
            bg_img_url=post_form.bg_img_url.data,
            body=post_form.body.data,
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=post_form, title="New Post")


# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<int:post_id>", methods=["POST", "GET"])
def edit_post(post_id):
    post = db.session.get(BlogPost, post_id)
    post_form = NewBlogForm(
        title=post.title,
        subtitles=post.subtitle,
        author=post.author,
        bg_img_url=post.img_url,
        body=post.body,
    )
    if post_form.validate_on_submit():
        post.title = post_form.title.data
        post.subtitle = post_form.subtitles.data
        post.author = post_form.author.data
        post.img_url = post_form.bg_img_url.data
        post.body = post_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template(
        "make-post.html", form=post_form, title=f"Edit Post #{post_id}"
    )


# TODO: delete_post() to remove a blog post from the database
@app.route("/delete_post/<int:post_id>", methods=["POST", "GET"])
def delete_post(post_id):
    post = db.session.get(BlogPost, post_id)
    db.session.delete(BlogPost, post)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
