import os
import json
import base64
from flask_dotenv import DotEnv
# Load library
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
nltk.download('punkt')
import constants
from constants import EXTENDED_STOPS, WIKI_URL, MAPS_URL, STATIC_MAP_URL, STATIC_PARAMS
import requests
from flask import request
from flask import Flask, render_template
from flask import send_from_directory
from nltk.tokenize import WordPunctTokenizer


app = Flask(__name__)
env = DotEnv(app)
env.init_app(app, env_file=".env", verbose_mode=True)
env.eval(keys={
  "MAPSKEY": str
})
print(app.config)
@app.route('/')
def index():
    """This function loads the template"""
    return render_template("chat.html")

@app.route('/favicon.ico')
def favicon():
    """This function is used to display favicon"""
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')

def get_wiki(location):
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
def get_coords(research):
    """This function uses the location entered by the user to find the coordinates"""
    location = json.loads(
        requests.get(
            f"{constants.GEOCODE_BASE}={research}+France&key={app.config['MAPSKEY']}").text)
    if len(location["results"]) == 0:
        return None
    #print(location.content)
    lat = location["results"][0]["geometry"]["location"]["lat"]
    lng = location["results"][0]["geometry"]["location"]["lng"]
    return lat, lng

def get_map(research,  location):
    """This function uses the user input and the dict of coordinates to retrieve a map"""
    if location is None:
        return "NO AVAILABLE IMAGE"
    lat = location[0]
    lng = location[1]
    map_image = requests.get(
        f"{constants.STATIC_MAP_URL}={research}&{constants.STATIC_PARAMS}:C%7C{lat},{lng}&key={app.config['MAPSKEY']}")
    return base64.b64encode(map_image.content).decode("UTF8")
# background process happening without any refreshing
@app.route('/input_process')
def input_process():
    """This function is used to communicate with the client-side of the application."""
    print("START START START START")
    stop = stopwords.words("french")
    stop.extend(constants.EXTENDED_STOPS)
    input_text = request.args.get('input_text')

    asked = nltk.word_tokenize(input_text)
    tokenizer = nltk.RegexpTokenizer('\w+')
    text_word = tokenizer.tokenize(input_text)

    process_words = [w for w in text_word if w not in stop]
    #words put in strings separated by "+" in the request of location
    research = "+".join(process_words)
    location = get_coords(research)
    map_img = get_map(research, location)
    wiki_desc = get_wiki(location)
    print(wiki_desc)

    return  {
                "result": f"data:image/png;base64,{map_img}",
                "wiki": str(wiki_desc)
            }




