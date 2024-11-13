import urllib.request
import html


def create_question_data(q_number):
    url = f"https://opentdb.com/api.php?amount={q_number}&type=boolean"

    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode("utf-8")
    dictionary = eval(text)
    question_data = dictionary["results"]

    for q in question_data:
        q["question"] = html.unescape(q["question"])
    return question_data
