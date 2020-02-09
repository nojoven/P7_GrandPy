import os
from flask import Flask, render_template
from flask import send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("chat.html")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')