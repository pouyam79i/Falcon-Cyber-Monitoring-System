# Importing required modules
from asyncio.windows_events import NULL
from telethon.sync import TelegramClient
import configparser
import datetime
import json

# importing for api route
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def read_conf():
    # reading config file
    config = configparser.ConfigParser()
    config.read("sys.ini")
    return config

# this method saves a json file
def save_json(data_list, file_address):
    # saving data into json file as raw data base
    try:
        with open(file_address + 'data.json', mode='w', encoding='utf8') as f:
            json.dump(data_list, f ,ensure_ascii=False, indent=4)
        return True
    except:
        return False

# this method modifies sys.ini
def modify_conf(limit=-1, date=-1):
    if limit < 0 and date == -1:
        return
    config = read_conf()
    if limit != -1:
        config.set('setting', 'limit', limit)
    if date != -1:
        config.set('setting', 'date', date)

# crawler method
@app.route('/crawl', methods=['GET'])
def crawl():

    # reading config files
    config = read_conf()
    # client configs
    api_id = config["client"]["api_id"]
    api_hash = config["client"]["api_hash"]
    # phone = config["client"]["phone"]
    username = config["client"]["username"]
    # database configs
    file_address = config["database"]["file_address"]
    # extractor config
    limit = config["setting"]["limit"]
    date = config["setting"]["date"]

    if date == 0:
        date = datetime.date.today()

    # exisiting channel info
    channeles = []
    channeles_name = {}

    # gathering channel infos
    with TelegramClient(username, api_id, api_hash) as client:
        for dialog in client.iter_dialogs():
            if dialog.is_group or dialog.is_channel:
                # print("Channel ID: " + str(dialog.id) + ", Channel Title: " + dialog.title)
                channeles.append(dialog.id)
                channeles_name['{}'.format(dialog.id)] = '{}'.format(dialog.title)

        # gathered data will be appended to this list
        data_list = []

        # iterating over today messages of channels 

        counter = 0
        for chat in channeles:    
            for message in client.iter_messages(chat, offset_date=date , reverse=True):

                # data format
                data = {
                "unique_id" : (str(chat) + '*' + str(message.id)),      # str
                "channel_id" : chat,                                    # int
                "channel_name" : channeles_name['{}'.format(chat)],     # str
                "id" : message.id,                                      # int
                "from_id" : str(message.from_id),                       # str or null
                "text" : message.text,                                  # str
                "date" : str(message.date),                             # str
                "views" : message.views,                                # int
                "forwards" : message.forwards,                          # int
                "edit_date" : str(message.edit_date)                    # str
                }
                # print(data)    
                data_list.append(data)
                
                counter = counter + 1
                if limit > 0:
                    if counter >= limit:
                        break

        # saving json file
        save_json(data_list, file_address)

        # returning jsonified result
        return jsonify(data_list)

# call this method to crawl telegram messages

# running flask app
app.run()