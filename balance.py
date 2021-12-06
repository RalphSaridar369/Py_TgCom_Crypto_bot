import requests
import telegram.ext
from functions import *
from telegram import *
import json
import math
import os
import random

api_key = "2121277949:AAGnsnht0fJVh_zrsybJdpuc9TgJn6YOo5c"
api_key_dev = "5079399379:AAFjP1KBQd7CIrgS2Mt8QSOMZjPWmb6Ovdw"
print("Bot running in tg")

updater = telegram.ext.Updater(api_key_dev,use_context=True)
disp = updater.dispatcher
disp.add_handler(telegram.ext.CommandHandler("start",start))
disp.add_handler(telegram.ext.CommandHandler("help",help))
disp.add_handler(telegram.ext.CommandHandler("about",content))
disp.add_handler(telegram.ext.CommandHandler("contact",contact))
disp.add_handler(telegram.ext.CommandHandler("balance",balance))
disp.add_handler(telegram.ext.CommandHandler("coinflip",coinflip))
disp.add_handler(telegram.ext.CommandHandler("lucky",luckyWinner))
disp.add_handler(telegram.ext.CommandHandler("pumpit",pumpit))
disp.add_handler(telegram.ext.CommandHandler("joke",joke))
disp.add_handler(telegram.ext.CommandHandler("ntek",ntek))
disp.add_handler(telegram.ext.CommandHandler("mybalance",myWallet))
disp.add_handler(telegram.ext.CommandHandler("yoda",yoda))
disp.add_handler(telegram.ext.CommandHandler("badbot",badbot))
disp.add_handler(telegram.ext.CommandHandler("give",giveaway))
disp.add_handler(telegram.ext.CommandHandler("stopgive",stopGiveaway))
disp.add_handler(telegram.ext.CommandHandler("wl",whitelist))
disp.add_handler(telegram.ext.CommandHandler("cal",calendar))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.filters.Filters.text, MessageHandler))
disp.add_handler(telegram.ext.CallbackQueryHandler(queryHandler))

updater.start_polling()
updater.idle()