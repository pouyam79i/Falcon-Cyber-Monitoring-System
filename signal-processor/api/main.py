import flask
from flask import request, jsonify
from analyzer import parse_text

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to FCMS's Analyzer</h1><p>Have a good time!</p>"


@app.route('/analyze', methods=['POST'])
def analyze():
    req = request.json
    out = []
    for post in req:
        val = parse_text(post['text'])
        out.append(val)
    return jsonify(str(out))


app.run()
