from flask import Flask
import random

app = Flask(__name__)

rand_num = random.randint(0, 9)
numbers_img = [
    '<iframe src="https://giphy.com/embed/7E3NdvP8aiPJodUDc7" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>',
    '<iframe src="https://giphy.com/embed/3oKIPrwk5SCKWexkLS" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>',
    '<iframe src="https://giphy.com/embed/26gsqQxPQXHBiBEUU" width="480" height="320" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>',
    '<iframe src="https://giphy.com/embed/NRtZEyZjbLgr0BJ4B8" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>',
    '<iframe src="https://giphy.com/embed/U7oYLyQqXM9sA" width="400" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>',
    '<iframe src="https://giphy.com/embed/LSKVlAGSnuXxVdp5wN" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>',
    '<iframe src="https://giphy.com/embed/L4NtmZmGB6zwUKPw6R" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>',
    '<iframe src="https://giphy.com/embed/l378atCG9uQQa1Fy8" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>',
    '<iframe src="https://giphy.com/embed/4KF4GmJwWrScU" width="400" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>',
    '<iframe src="https://giphy.com/embed/6OyrnAKxd46Rfall6K" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>',
]
high_img = '<iframe src="https://giphy.com/embed/wHB67Zkr63UP7RWJsj" width="480" height="337" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'
low_img = '<iframe src="https://giphy.com/embed/dKpEvFHdGsZBRuszpv" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'


@app.route("/")
def main():
    return (
        "<h1>Guess a number between 0 and 9</h1>"
        '<iframe src="https://giphy.com/embed/fAo1Tv1OGE6AQZ2s0T" width="480" height="479" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'
    )


@app.route("/<int:num_pick>")
def num_page(num_pick):
    if int(num_pick) == rand_num:
        return (
            "<h1 style='color: green';>You found me!</h1>"
            f"{numbers_img[int(num_pick)]}"
        )
    elif int(num_pick) > rand_num:
        return "<h1 style='color: purple';>Too high, try again!</h1>" f"{high_img}"
    else:
        return "<h1 style='color: red';>Too low, try again!</h1>" f"{low_img}"


if __name__ == "__main__":
    app.run(debug=True)
