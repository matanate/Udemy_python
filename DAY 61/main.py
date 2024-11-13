from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5


class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        label="Password", validators=[DataRequired(), Length(min=8, max=20)]
    )
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "ghfgjnghjkmhfmnh"
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    email = login_form.email.data
    password = login_form.password.data
    if login_form.validate_on_submit():
        if email == "admin@email.com" and password == "12345678":
            return redirect("success.html")
        else:
            return redirect("denied.html")

    return render_template("login.html", form=login_form)


if __name__ == "__main__":
    app.run(debug=True)
