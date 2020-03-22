"""
This Class has methods that can be called in the process method in main.py:
- get_input(process_words)
- process_words()
- get_coords(research)
- get_map(research,  location)
- get_wiki(location)
"""
import json
import base64
import requests
import nltk
import constants
from nltk.corpus import stopwords
nltk.download("stopwords")
nltk.download("punkt")


class Reactions:
    """The class is used to respond to the user"""
    def get_input(self, process_words):
        """
            Formatting words to write an URL (for GET HTTP request)
            Words are put in strings separated by "+"
            in the request of location.
        """
        research = "+".join(process_words)
        return research

    def get_coords(self, research, conf):
        """This function uses the location entered by the user to find the coordinates"""
        location = json.loads(
            requests.get(
                f"{constants.GEOCODE_BASE}={research}+France&key={conf['MAPSKEY']}"
            ).text
        )
        print(location)
        if len(location["results"]) == 0:
            return None
        # print(location.content)
        lat = location["results"][0]["geometry"]["location"]["lat"]
        lng = location["results"][0]["geometry"]["location"]["lng"]
        return lat, lng

    def get_map(self, research, location, conf):
        """
            This function uses the user input and the dict of coordinates
            to retrieve a map.
        """
        if location is None:
            return "NO AVAILABLE IMAGE"
        lat = location[0]
        lng = location[1]
        # It gets the image from the api
        map_image = requests.get(
            f"{constants.STATIC_MAP_URL}={research}&{constants.STATIC_PARAMS}\
            :C%7C{lat},{lng}&key={conf['MAPSKEY']}"
        )
        # Converts the image into a base64 format (base64 is string), then retuns the string
        return base64.b64encode(map_image.content).decode("UTF8")

    def get_wiki(self, location):
        """
            This function uses coordiates to retrieve the summary
            of the first matching article
        """
        if location is None:
            return "J'connais pas ce coin là, Gamin..."
        lat = location[0]
        lng = location[1]
        json_wiki = json.loads(requests.get(f"{constants.WIKI_URL}{lat}|{lng}").text)
        if len(json_wiki["query"]["pages"].values()) == 0:
            return "J'connais pas trop, Gamin..."
        return list(json_wiki["query"]["pages"].values())[0]["extract"]

    def process_words(self, input_text):
        """
            This function processes the raw input.
            It takes a string and returns a list of meaningful words.
        """
        stop = stopwords.words("french")
        stop.extend(constants.EXTENDED_STOPS)
        tokenizer = nltk.RegexpTokenizer(r"\w+")
        text_word = tokenizer.tokenize(input_text)

        process_words = [w for w in text_word if w not in stop]
        return process_words
