from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)
my_name = "Matan Atedgi"


@app.route("/")
def home():
    current_year = datetime.date.today().year
    rand_num = random.randint(1, 10)
    return render_template(
        "index_home.html", rand_num=rand_num, current_year=current_year, name=my_name
    )


@app.route("/guess/<name>")
def guess(name):
    current_year = datetime.date.today().year
    response = requests.get(f"https://api.agify.io?name={name}")
    age = response.json()["age"]
    response = requests.get(f"https://api.genderize.io?name={name}")
    gender = response.json()["gender"]

    return render_template(
        "index_guess.html",
        age=age,
        name=name,
        gender=gender,
        my_name=my_name,
        current_year=current_year,
    )


@app.route("/blog/<num>")
def get_blog(num):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template("blog.html", all_posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
