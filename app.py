from flask import Flask, Response, request, render_template
from flask_bootstrap import Bootstrap
from password import *

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index():
    return render_template("index.html.j2")

@app.route("/processform")
def processform():
    easy_typing = request.args.get("easy_typing")

    if easy_typing == "on":
        all_words = read_file("words.txt")
        all_words = type_easy(all_words)
    else:
        all_words = read_file("words.txt")

    min_length = request.args.get("min_length")
    max_length = request.args.get("max_length")
    num_sub = request.args.get("num_sub")
    min_word_length = request.args.get("min_word_length")
    max_word_length = request.args.get("max_word_length")
    all_pswds = generate_pswds(all_words,int(min_length),int(max_length),int(min_word_length), int(max_word_length), 4,80)

    if num_sub == "on":
        all_pswds = number_substitution(all_pswds)

    all_pswds = check_passwords(all_pswds)

    return render_template("list.html.j2", pswds=all_pswds)


if __name__ == '__main__':
    app.run(debug=True)
