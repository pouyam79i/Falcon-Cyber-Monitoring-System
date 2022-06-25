# Importing required modules
from telethon.sync import TelegramClient
import configparser
import datetime
import json

# reading config file
config = configparser.ConfigParser()
config.read("sys.ini")

# client configs
api_id = config["client"]["api_id"]
api_hash = config["client"]["api_hash"]
phone = config["client"]["phone"]
username = config["client"]["username"]

# data base configs
filename = config["database"]["file_address"]

# crawler method
def crawl():

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
        for chat in channeles:    
            for message in client.iter_messages(chat, offset_date=datetime.date.today() , reverse=True):
                # data format
                data = {
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

        # saving data into json file as raw data base
        with open(filename, mode='w', encoding='utf8') as f:
            json.dump(data_list, f ,ensure_ascii=False, indent=4)

# call this method to crawl telegram messages
crawl() 
