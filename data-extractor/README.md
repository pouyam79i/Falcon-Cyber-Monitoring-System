# Data Extractor
This code crawls messages of channels you have joined.

# Installation
Clone this repo then go to 'data_extractor' directory.<br>
Inside directory 'data_extractor' you should do a few changes:<br>
 * rename 'sys.ini.example' to 'sys.ini'
 * inside file 'sys.ini' put your own api_id, api_hash, username, phone (number)
 * make sure that the crawl() function is called at the end of file of 'crawler.py'

After doing what is said above run these commands in terminal (You should be in 'data_extractor' directory):

    pip install telethon
    python crawler.py


# Note
To get 'api_id' and 'api_hash' go to this <a href="https://my.telegram.org/">link</a>.
