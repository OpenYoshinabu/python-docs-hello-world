from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!\nThis part is changed just for trying to use Azure app aservice."
