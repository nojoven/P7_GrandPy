import pytest
import os
import json
import base64
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
nltk.download('punkt')
import requests
import constants
import Reactions
from constants import EXTENDED_STOPS, WIKI_URL, MAPS_URL, STATIC_MAP_URL, STATIC_PARAMS
from flask import request
from flask import Flask, render_template
from flask import send_from_directory
from nltk.tokenize import WordPunctTokenizer
from flask_dotenv import DotEnv

class Test_Reactions:
    input_text = "GrandPy connais-tu l' Arc de Triomphe ?"
    conf = os.environ
    rX = Reactions.Reactions()

    def test_process_words(self):
        process_words = self.rX.process_words(self.input_text)
        assert isinstance(process_words, list)
        assert len(process_words) > 0
        for word in process_words:
            assert isinstance(word, str)

    def test_get_input_(self):
        process_words = self.rX.process_words(self.input_text)
        research = self.rX.get_input(process_words)
        assert research == "+".join(process_words)

    def test_get_coords(self):
        process_words = self.rX.process_words(self.input_text)
        research = self.rX.get_input(process_words)
        print(research)
        print(self.conf)
        coords = self.rX.get_coords(research, self.conf)
        assert coords is not None
        assert len(coords) == 2

    def test_get_map(self):
        process_words = self.rX.process_words(self.input_text)
        research = self.rX.get_input(process_words)
        location = self.rX.get_coords(research, self.conf)
        map_img = self.rX.get_map(research, location, self.conf)
        assert map_img is not None
        assert isinstance(map_img, str)

    def test_get_wiki(self):
        process_words = self.rX.process_words(self.input_text)
        research = self.rX.get_input(process_words)
        location = self.rX.get_coords(research, self.conf)
        wiki_desc = self.rX.get_wiki(location)
        assert isinstance(wiki_desc, str)
        assert len(wiki_desc) > 0





