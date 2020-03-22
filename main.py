"""This is the entry point of the application"""
import os
from flask import Flask, render_template, request
import reactions
import nltk
nltk.download("stopwords")
nltk.download("punkt")


"""Initializes the Flask app"""
APP = Flask(__name__)

CONF = os.environ
"""Set environment variables without sending it on github"""


@APP.route("/")
def index():
    """
        This function loads the template
        When someone tries to access the route '/'
        flask calls this function
    """
    return render_template("chat.html")


@APP.route("/input_process")
def input_process():
    """
        When someone tries to access the route /input_process,
        Flask calls this function.
        This function is used to communicate
        with the client-side of the application.
        Background process happening without refreshing
    """
    print("START START START START")

    rx = reactions.Reactions()
    input_text = request.args.get("input_text")
    process_words = rx.process_words(input_text)
    research = rx.get_input(process_words)
    location = rx.get_coords(research, CONF)
    map_img = rx.get_map(research, location, CONF)
    wiki_desc = rx.get_wiki(location)
    print(location)
    print(wiki_desc)
    # A JSON is returned to the client which waits for JSON
    return {"result": f"data:image/png;base64,{map_img}", "wiki": str(wiki_desc)}
