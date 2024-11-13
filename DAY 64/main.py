from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired
import requests

"""
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
"""


class EditRatingForm(FlaskForm):
    rating = StringField(label="Your Rating out of 10 e.g. 7.5")
    review = StringField(label="your Review")
    submit = SubmitField(label="Done")
    id = HiddenField()


class AddForm(FlaskForm):
    movie_title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
bootstrap = Bootstrap5(app)

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Top-Movies.db"
db.init_app(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String, nullable=True)
    img_url = db.Column(db.String, nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    all_movies = list(
        db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars()
    )
    for i, movie in enumerate(all_movies):
        movie.ranking = len(all_movies) - i
        db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["POST", "GET"])
def edit():
    edit_form = EditRatingForm()
    movie_id = request.args.get("id")
    if edit_form.validate_on_submit():
        movie_to_update = db.get_or_404(Movie, movie_id)
        movie_to_update.rating = edit_form.rating.data
        movie_to_update.review = edit_form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    movie_selected = db.get_or_404(Movie, movie_id)
    return render_template("edit.html", movie=movie_selected, form=edit_form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["POST", "GET"])
def add():
    add_form = AddForm()
    if add_form.validate_on_submit():
        movie_title = add_form.movie_title.data
        return redirect(url_for("select", movie_title=movie_title))
    return render_template("add.html", form=add_form)


@app.route("/select")
def select():
    movie_title = request.args.get("movie_title")
    url = f"https://api.themoviedb.org/3/search/movie?query={movie_title}&include_adult=false&language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmM2JjZjZjODAxYmVkN2MxZmI3ZjFhYWUzMjA5YTA0NSIsInN1YiI6IjY1NjFlNzZkMDI4ZjE0MDBlMTMwMGE1MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.1D_YHIkN3RN9MsmKV91ugao9VfkWuBWhVIB1bvgIL6E",
    }
    response = requests.get(url, headers=headers).json()["results"]
    movies_list = []
    for movie in response:
        movies_list.append(
            {
                "title": movie["title"],
                "release_date": movie["release_date"],
                "year": movie["release_date"].split("-")[0],
                "overview": movie["overview"],
                "img_url": f"https://www.themoviedb.org/t/p/w600_and_h900_bestv2{movie['poster_path']}",
            }
        )
    return render_template("select.html", movies_list=movies_list)


@app.route("/fetch")
def fetch():
    title = request.args.get("title")
    year = int(request.args.get("year"))
    description = request.args.get("description")
    img_url = request.args.get("img_url")
    movie_obj = Movie(title=title, year=year, description=description, img_url=img_url)
    db.session.add(movie_obj)
    db.session.commit()
    id = movie_obj.id
    return redirect(url_for("edit", id=id))


if __name__ == "__main__":
    app.run(debug=True)
