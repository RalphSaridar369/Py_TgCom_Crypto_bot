import requests
import telegram.ext
from telegram import *
from datetime import date
import math
import random
import shelve
from uuid import uuid4
from telegram.utils.helpers import escape_markdown
from functions.globals import *
import json
from threading import Timer
from time import sleep

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

def outputMessage(data):
    return '''
    <b>Sohyoune l zaber</b>\nbought or minted this:\n\n<b>Contract address:</b> {}\n<b>NFT Name:</b> {}\n<b>URL:</b> {}\n 
    '''.format(data['contractAddress'],data['tokenName'],'https://opensea.io/{}'.format(data['tokenName']))    

def printit (update,context):
    print("running")
    url = '''https://api.polygonscan.com/api?module=account&action=tokennfttx&address={}&startblock=0&endblock=99999999&page=1&sort=asc&apikey={}'''.format(add,pol_key)# print(url)
    page = requests.get(url)
    res = page.json()
    results = res['result']
    f = open('./write.txt','w')
    f.write(str(results[len(results)-15]))
    f.close()
    print(results[len(results)-1])
    message = outputMessage(results[len(results)-1])
    update.message.reply_text(message,parse_mode=ParseMode.HTML)
    # real_balance = str("{0:.2f}".format(float(res['result'])/math.pow(10,18)))+" Matic"
    # update.message.reply_text(real_balance)
    
def startList(update,context):
    rt = RepeatedTimer(10.0, printit, update,context) # it auto-starts, no need of rt.start()
    

pol_key = "SIZEEU48BVGR4U9UHWQ8S5DXT8N9IMMZ8V"
add = "0x06761b0097c5f658bd368b453b330f7e26a5ea7e"
my_add = "0x70705002Fc8c4366ccA07552d72346ec5e5F5530"