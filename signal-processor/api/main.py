import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

telegram_sample_post = {
    "message_id": 5,
    "from": {
        "id": 557543219,
        "is_bot": False,
        "first_name": "PM",
        "username": "Poya_moh",
        "language_code": "en"
    },
    "chat": {
        "id": 557543219,
        "first_name": "PM",
        "username": "Poya_moh",
        "type": "private"
    },
    "date": 1653410523,
    "text": "[ Photo ]\n🏦 آخرین بروز رسانی نرخ ارز در صرافی بانک ملی\n  \n  🗓 چهارشنبه مورخ: 1401/01/31\n  ⏰ ساعت: 14:32\n  \n  🔵 خرید #دلار 25,042 (18+)\n  🔴 فروش دلار 25,293.60 (18.20+) ✅\n  \n  🔵 خرید #یورو 28,427.20 (23.40+) ✅\n  🔴 فروش یورو 28,712.90 (23.70+)\n\n\n📱(021) 91015575\n🌐 www.sahamyab.com\n🆔 @sahamyab",
    "entities": [
        {"offset": 119, "length": 5, "type": "hashtag"},
        {"offset": 187, "length": 5, "type": "hashtag"},
        {"offset": 270, "length": 16, "type": "url"},
        {"offset": 290, "length": 9, "type": "mention"}
    ]
}

a = []


@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to FCMS's Analyzer</h1><p>Have a good time!</p>"


@app.route('/analyze', methods=['POST'])
def analyze():
    print("Shit!!!!!!")
    print(request.json)
    return request.json


app.run()
