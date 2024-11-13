from flask import Flask, render_template, redirect, flash, url_for
from flask_bootstrap import Bootstrap5
from cafeform import CafeForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
import time

DB_URL = "sqlite:///cafes.db"

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
bootstrap = Bootstrap5(app)

app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cafe = db.Column(db.String(100), unique=False, nullable=False)
    location = db.Column(db.String(1000), unique=False, nullable=False)
    open_time = db.Column(db.Time, unique=False, nullable=False)
    close_time = db.Column(db.Time, unique=False, nullable=False)
    coffee_rating = db.Column(db.String(20), unique=False, nullable=False)
    wifi_rating = db.Column(db.String(20), unique=False, nullable=False)
    power_avail = db.Column(db.String(20), unique=False, nullable=False)


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()

    if form.validate_on_submit():
        review = Reviews(
            cafe=form.cafe.data.title(),
            location=form.location.data,
            open_time=form.open_time.data,
            close_time=form.close_time.data,
            coffee_rating=form.coffee_rating.data,
            wifi_rating=form.wifi_rating.data,
            power_avail=form.power_avail.data,
        )
        db.session.add(review)
        db.session.commit()
        flash("Cafe Submitted!", "info")
        return redirect(url_for("add_cafe"))
    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    cafes = db.session.query(Reviews).all()
    titles = ["Cafe Name", "Location", "Open", "Close", "Coffee", "Wifi", "Power"]
    return render_template("cafes.html", cafes=cafes, titles=titles)


if __name__ == "__main__":
    app.run(debug=True)
