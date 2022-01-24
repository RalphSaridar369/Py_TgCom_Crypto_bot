import requests
import telegram.ext
from functions.main import *
from functions.giveaway import *
from functions.inlinequeryhandler import *
from functions.messagehandler import *
from functions.queryhandler import *
from functions.whitelist import *
from telegram import *
import json
import math
import os
import random
import shelve

api_key_dev = "2121277949:AAGnsnht0fJVh_zrsybJdpuc9TgJn6YOo5c"
api_key = "5141608151:AAHgvSJfTpDx5d-fTsUUNrjuvI_x4UKMEFA"

print("Bot running in tg")

updater = telegram.ext.Updater(api_key)
disp = updater.dispatcher
disp.add_handler(telegram.ext.CommandHandler("start",start))
disp.add_handler(telegram.ext.CommandHandler("guide",guide))
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
disp.add_handler(telegram.ext.CommandHandler("adminpanel",adminpanel))
disp.add_handler(telegram.ext.CommandHandler("meme",meme))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.filters.Filters.text, MessageHandler))
disp.add_handler(telegram.ext.CallbackQueryHandler(queryHandler))
disp.add_handler(telegram.ext.InlineQueryHandler(InlineQueryHandler))
# disp.add_handler(telegram.ext.ChosenInlineResultHandler(chosenInline))

updater.start_polling()
updater.idle()
