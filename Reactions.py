"""
This Class has methods that can be called in the process method in main.py:
- get_coords(research)
- get_map(research,  location)
- get_wiki(location)
"""
import os
import json
import base64
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
nltk.download('punkt')
import requests
import constants
from constants import EXTENDED_STOPS, WIKI_URL, MAPS_URL, STATIC_MAP_URL, STATIC_PARAMS
from flask import request
from flask import Flask, render_template
from flask import send_from_directory
from nltk.tokenize import WordPunctTokenizer
from flask_dotenv import DotEnv


class Reactions:
    """The class is used to respond to the user"""

    def get_input(self, process_words):
        # words put in strings separated by "+" in the request of location
        research = "+".join(process_words)
        return research

    def get_coords(self, research, conf):
        """This function uses the location entered by the user to find the coordinates"""
        location = json.loads(
            requests.get(
                f"{constants.GEOCODE_BASE}={research}+France&key={conf['MAPSKEY']}").text)
        if len(location["results"]) == 0:
            return None
        # print(location.content)
        lat = location["results"][0]["geometry"]["location"]["lat"]
        lng = location["results"][0]["geometry"]["location"]["lng"]
        return lat, lng

    def get_map(self, research, location, conf):
        """This function uses the user input and the dict of coordinates to retrieve a map"""
        if location is None:
            return "NO AVAILABLE IMAGE"
        lat = location[0]
        lng = location[1]
        map_image = requests.get(
            f"{constants.STATIC_MAP_URL}={research}&{constants.STATIC_PARAMS}:C%7C{lat},{lng}&key={conf['MAPSKEY']}")
        return base64.b64encode(map_image.content).decode("UTF8")

    def get_wiki(self, location):
        """This function uses coordiates to retrieve the summary of the first matching article"""
        if location is None:
            return "J'connais pas ce coin là, Gamin..."
        lat = location[0]
        lng = location[1]
        json_wiki = json.loads(
            requests.get(
                f"{constants.WIKI_URL}{lat}|{lng}").text
        )
        if len(json_wiki["query"]["pages"].values()) == 0:
            return "J'connais pas trop, Gamin..."
        return list(json_wiki["query"]["pages"].values())[0]["extract"]

    def process_words(self):
        stop = stopwords.words("french")
        stop.extend(constants.EXTENDED_STOPS)
        input_text = request.args.get('input_text')
        tokenizer = nltk.RegexpTokenizer('\w+')
        text_word = tokenizer.tokenize(input_text)

        process_words = [w for w in text_word if w not in stop]
        return process_words