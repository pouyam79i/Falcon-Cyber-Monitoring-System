# Importing required modules
# from telethon.sync import TelegramClient
import sys
from unittest import result
from telethon.sync import TelegramClient
import configparser
from datetime import date as datetime, timedelta
import json
from aiohttp import web
import re

# main code:


def read_conf():
    # reading config file
    try:
        config = configparser.ConfigParser()
        config.read("sys.ini")
        return config
    except:
        print("Failed to read sys.ini files")
        return False


# this method saves a json file
def save_json(data_list, file_address):
    # saving data into json file as raw data base
    try:
        with open(file_address + 'data.json', mode='w', encoding='utf8') as f:
            json.dump(data_list, f, ensure_ascii=False, indent=4)
        return True
    except:
        print("Cannot save json file")
        return False


# this method modifies sys.ini
def modify_conf(limit=-1, date=-1):
    if limit < 0 and date == -1:
        return
    config = read_conf()
    if config is False:
        print("Cannot modify 'sys.ini'. reason: cannot read config!")
        return
    if limit != -1:
        config.set('setting', 'limit', str(limit))
    if date != -1:
        config.set('setting', 'date', str(date))
    try:
        with open('sys.ini', 'w') as configfile:
            config.write(configfile)
    except:
        print("Cannot modify 'sys.ini'. reason: cannot write file")
        print("Detail: ", sys.exc_info()[0], "occured")
        return


# crawler functionality
async def crawl():
    # reading config files
    config = read_conf()
    if config is False:
        print("Cannot crawl! reason: cannot read config info")
        return {"attempt": "failed", "reason": "cannot read sys.ini"}

    # client configs
    api_id = config.get("client", "api_id")
    api_hash = config.get("client", "api_hash")
    # phone = config["client"]["phone"]
    username = config.get("client", "username")
    # database configs
    file_address = config.get("database", "file_address")
    # extractor config
    limit = int(config.get("setting", "limit"))
    date = config.get("setting", "date")
    if date is '0':
        date = datetime.today()
    print(date)

    # exisiting channel info
    channeles = []
    channeles_name = {}

    try:
        # gathering channel infos
        async with TelegramClient(username, api_id, api_hash) as client:
            async for dialog in client.iter_dialogs():
                if dialog.is_group or dialog.is_channel:
                    # print("Channel ID: " + str(dialog.id) + ", Channel Title: " + dialog.title)
                    channeles.append(dialog.id)
                    channeles_name['{}'.format(
                        dialog.id)] = '{}'.format(dialog.title)

            # gathered data will be appended to this list
            data_list = []

            # iterating over today messages of channels

            counter = 0
            for chat in channeles:
                async for message in client.iter_messages(chat, offset_date=date, reverse=True):

                    # data format
                    message_date_str = str(message.date)
                    message_date, time, timezone = re.split(
                        r'[T\s\+]', message_date_str)
                    data = {
                        # str
                        "unique_id": (str(chat) + '*' + str(message.id)),
                        "channel_id": chat,  # int
                        # str
                        "channel_name": channeles_name['{}'.format(chat)],
                        "id": message.id,  # int
                        "from_id": str(message.from_id),  # str or null
                        "text": message.text,  # str
                        "date": message_date,  # str
                        'time': time,
                        'timezone': timezone,
                        "views": message.views,  # int
                        "forwards": message.forwards,  # int
                        "edit_date": str(message.edit_date)  # str
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
            return data_list
    except Exception as err:
        print('ERR', err)
        # print("Cannot crawl data! ", sys.exc_info()[0], " occured!")
        # return {"attempt": "failed", "reason": "not defined!"}
        pass


# call this method to crawl telegram messages

routes = web.RouteTableDef()


@routes.get('/crawl')
async def crawler(request):
    result = await crawl()
    return web.json_response(result)


app = web.Application()
app.add_routes(routes)
web.run_app(app)
