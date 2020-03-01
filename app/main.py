import os
import json
import base64
# Load library
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
nltk.download('punkt')
import constants
import requests
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

def get_coords(process_words):
    research = "+".join(process_words)

    location = json.loads(
        requests.get(
            f"https://maps.googleapis.com/maps/api/geocode/json?address={research}&key={constants.MAPSKEY}").text)
    #print(location.content)
    lat = location["results"][0]["geometry"]["location"]["lat"]
    lng = location["results"][0]["geometry"]["location"]["lng"]
    print(f"lat = {lat}, lng = {lng}")
    map_image = requests.get(
        f"https://maps.googleapis.com/maps/api/staticmap?center={research}&zoom=13&size=300x150&maptype=roadmap&markers=color:red%7Clabel:C%7C{lat},{lng}&key={constants.MAPSKEY}")
    return base64.b64encode(map_image.content).decode("UTF8")
# background process happening without any refreshing
@app.route('/input_process')
def input_process():
    print("START START START START")
    stop = stopwords.words("french")
    stop.extend(constants.EXTENDED_STOPS)
    input_text = request.args.get('input_text')

    asked = nltk.word_tokenize(input_text)
    tokenizer = nltk.RegexpTokenizer('\w+')
    text_word = tokenizer.tokenize(input_text)
    print(text_word)
    process_words = [w for w in text_word if w not in stop]
    #words put in strings separated by "+" in the request of location
    print(process_words)
    encoded = get_coords(process_words)

    return {"result": f"data:image/png;base64,{encoded}"}




