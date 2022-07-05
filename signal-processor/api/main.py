import flask
from flask import request, jsonify
from analyzer import parse_text


def startAPI():
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
            val = parse_text(post)
            if val is not None:
                out.append(val.serialize())
        return jsonify(out)

    app.run()


if __name__ == '__main__':
    startAPI()
