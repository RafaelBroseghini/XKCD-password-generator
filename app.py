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
    language = request.args.get("language")

    if easy_typing == "on":
        all_words = read_file("static/languages/"+language)
        all_words = type_easy(all_words)
    else:
        all_words = read_file("static/languages/"+language)

    min_length = int(request.args.get("min_length"))
    max_length = int(request.args.get("max_length"))
    num_sub = request.args.get("num_sub")
    min_word_length = int(request.args.get("min_word_length"))
    max_word_length = int(request.args.get("max_word_length"))
    all_pswds = generate_pswds(all_words, min_length, max_length, min_word_length,  max_word_length, 4)

    if num_sub == "on":
        all_pswds = number_substitution(all_pswds)

    return render_template("list.html.j2", pswds=all_pswds)


if __name__ == '__main__':
    app.run(debug=True)
