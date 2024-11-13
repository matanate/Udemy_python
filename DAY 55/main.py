from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapped_function():
        return "<b>" + function() + "</b>"

    return wrapped_function


def make_emphasis(function):
    def wrapped_function():
        return "<em>" + function() + "</em>"

    return wrapped_function


def make_underline(function):
    def wrapped_function():
        return "<u>" + function() + "</u>"

    return wrapped_function


@app.route("/")
def hello():
    return "<h1 style='text-align: center'>Hello World!</h1> \
                <p style='text-align: center'>This is a paragraph.</p>\
                <img src='https://www.petage.com/wp-content/uploads/2019/09/Depositphotos_74974941_xl-2015-e1569443284386.jpg' width=200>"


@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye!"


@app.route("/username/<user>/<int:number>")
def username(user, number):
    return f"Hello {user} {number}"


if __name__ == "__main__":
    app.run(debug=True)
