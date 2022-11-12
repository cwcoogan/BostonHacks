"""
Python Flask Workshop - Chrome Extensions
"""

from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)

# allows front/back end to communicate
CORS(app)

@app.route("/")
def test():
    return  "Hello"

if __name__ == "__main__":
    app.run(debug = True)
