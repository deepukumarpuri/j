import random

from flask import Flask, jsonify, render_template

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def openedLink():
    result = {"OWNER": "https://t.me/DKBOTZHELP",
              "try": "/hindiJokes After the url to get a random joke and /hindiJokes/word to get the joke containing given word"}
    return result


@app.route('/hindiJokes/<string:st>')
def tellJoke(st):
    jokes = open('hindiJokes.txt', encoding='utf-8').read().splitlines()
    strJokes = []
    # check if the string is in the line or not
    for joke in jokes:
        if st in joke:
            strJokes.append(joke)
    if len(strJokes) != 0:
        showJoke = random.choice(strJokes)
        return '<html><head></head><body>' + showJoke + '</body></html>'
    else:
        notFound = {"notFound": "Sorry, There is no joke containing this word. You can read some other funny jokes",
                    "try_again": "if you are not sure which string to use just remove string and you will get a nice "
                                 "joke",
                    "demo_words": "you can try hindi words like मेरे, उनकी"}
        result = notFound
        return jsonify(result)


@app.route('/hindiJokes/')
def tellJokeRandom():
    jokes = open('hindiJokes.txt', encoding='utf-8').read().splitlines()
    showJoke = random.choice(jokes)
    while showJoke == "":
        showJoke = random.choice(jokes)
    result = {
        "joke": showJoke
    }
    return '<html><head></head><body>' + showJoke + '</body></html>'


if __name__ == '__main__':
    app.run(debug=True)
