import os
import json
import base64
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
nltk.download('punkt')
import Reactions
import requests
import constants
from constants import EXTENDED_STOPS, WIKI_URL, MAPS_URL, STATIC_MAP_URL, STATIC_PARAMS
from flask import request
from flask import Flask, render_template
from flask import send_from_directory
from nltk.tokenize import WordPunctTokenizer

"""Initializes the Flask app"""
app = Flask(__name__)
"""Set environment variables without sending it on github"""
conf = os.environ
print(conf)

"""When someone tries to access the route '/' flask calls this function"""
@app.route('/')
def index():
    """This function loads the template"""
    return render_template("chat.html")

"""When someone tries to access the route /input_process flask calls this function"""
@app.route('/input_process')
def input_process():
    """
        This function is used to communicate with the client-side of the application.
        Background process happening without refreshing
    """
    print("START START START START")

    rx = Reactions.Reactions()
    process_words = rx.process_words()
    research = rx.get_input(process_words)
    location = rx.get_coords(research, conf)
    map_img = rx.get_map(research, location, conf)
    wiki_desc = rx.get_wiki(location)
    print(location)
    print(wiki_desc)

    return  {
                "result": f"data:image/png;base64,{map_img}",
                "wiki": str(wiki_desc)
            }


