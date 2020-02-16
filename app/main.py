import os
from flask import request
from flask import Flask, render_template
from flask import send_from_directory
from nltk.tokenize import WordPunctTokenizer

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("chat.html")


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


# background process happening without any refreshing
@app.route('/input_process')
def input_process():
    input_text = request.args.get('input_text')
    words_in_question = WordPunctTokenizer().tokenize(input_text)
    print(words_in_question)




