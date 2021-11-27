import requests
import telegram.ext
from telegram import *
import json
import math
import random

api_key = "2121277949:AAGnsnht0fJVh_zrsybJdpuc9TgJn6YOo5c"
chat_id = -1001775758804
COIN_FLIP = ["Head","Tails"]
ABOUT_US_MESSAGE = """** Lebanese DeFi **\n\nWelcome to the group

We are working on building a community

La ne2dar kelna na3mol profits w nse3ed ba3ed at the end of the day

From token whitelists to presales  to launch dates to even NFTs"""
print("Bot running in tg")

def start(update, context):
	update.message.reply_text("Hello! Welcome to Lebanese DeFi!")

def badbot(update, context):
	arr = ["Sorry :(","Won't happen again","My bad","Please don't hurt my family"]
	update.message.reply_text(arr[random.randint(0,len(arr)-1)])


def joke(update, context):
	#page = requests.get("https://v2.jokeapi.dev/joke/Dark,Pun?blacklistFlags=nsfw,religious,political,racist,sexist,explicit",headers={"Accept":"application/json"})
	page = requests.get("https://api.yomomma.info/",headers={"Accept":"application/json"})
	res= page.json()
	#joke = res["setup"]+" "+res["delivery"]
	joke = res["joke"]
	update.message.reply_text(joke)

def myWallet(update, context):

	message = update.message["text"]
	hex = message.split(" ")[1]

	page = requests.get("https://api.bscscan.com/api?module=account&action=balance&address="+hex+"&apikey=T7YH7MHHQTPEB25EVTQH5Z7R5H1QK1KVXT")

	res = page.json()
	print("{:.18f}".format(float(res["result"])))
	update.message.reply_text("**Your Balance:**\n"+str(float(res['result'])/math.pow(10,18))+" BNB")

def yoda(update,context):

	message = update.message["text"]
	print("MESS: ",message)
	text = message.split("_")[1]
	page = requests.get("https://api.funtranslations.com/translate/yoda.json?text="+text)
	res = page.json()
	print("RES: ",res)
	update.message.reply_text(res["contents"]["translated"])
		

def ntek(update, context):
	#data = json.loads(update.message)
	print(update.message.from_user.first_name)
	name = update.message.from_user.first_name
	#fn = str(update.message[13])
	arr=[str("Merci ya "+name),str("Salty "+name),":(","3rase ya Damme"]
	update.message.reply_text(arr[random.randint(0,3)])

def luckyWinner(update, context):
	print(update.message["text"])
	message = update.message["text"]
	winnersLn = int(message.split(" ")[1])
	users = message.split(" ")[2].split("-")
	print("ln: ",len(users),type(users))
	winners = "** Winners **\n\n"
	for i,n in enumerate(range(winnersLn)):
		choice = random.randint(0,len(users)-1)
		print(choice)
		winners += str(n+1) +" - "+ users[choice]+"\n"
		users.pop(choice)

	winners += "\n\n Congrats !! "
	update.message.reply_text(winners)
	#print(bot)
	#choice = bot.getChatMemberCount(-1001775758804)
	#print(bot.getChatMember(chat_id,choice))

def help(update, context):
	update.message.reply_text("""
		The following commands are available:
		/balance => Gives balance of community's wallet
		/about => About Us
		/coinflip => Head or Tails
		/ntek => for ntek purposes
		/joke => sends a Yo mama joke
		/myWallet => sends your own wallet balance
	""")

def pumpit(update, context):
	for i in range(0,2):
		message=""
		if(i%2==0):
			message="Don't you know pump it up?"
		else:
			message="You've got to pump it up"
		
		update.message.reply_text(message.upper())

def content(update, context):
	update.message.reply_text(ABOUT_US_MESSAGE)

def coinflip(update, context):
	update.message.reply_text(COIN_FLIP[random.randint(0,1)])

def contact(update, context):
	update.message.reply_text("Admins")

def balance(update, context):

	address ="0xe57877431965F7f9EE9599E729497f33C0A1f48d"
	page = requests.get("https://api.bscscan.com/api?module=account&action=balance&address="+address+"&apikey=T7YH7MHHQTPEB25EVTQH5Z7R5H1QK1KVXT")

	res = page.json()
	print("{:.18f}".format(float(res["result"])))
	update.message.reply_text("**Community Balance:**\n"+str(float(res['result'])/math.pow(10,18))+" BNB")

def callback():
	print("test")

def giveaway(update, context):
	message = update.message["text"]
	print("MESSAGE: ",message)
	giveawayName = message.split(" ")[1]
	winnersLn = int(message.split(" ")[3])
	participantsLn = int(message.split(" ")[2])
	print("Test")
	button = [[InlineKeyboardButton("Join",callback_data="join_giveaway")]]
	context.bot.send_message(chat_id=update.effective_chat.id, text="Giveaway "+giveawayName+"\n\n\nNum of Participants: "+str(participantsLn)+"\nNum of Winners: "+str(winnersLn),
	 reply_markup=InlineKeyboardMarkup(button))

def MessageHandler(update, context):
	message = update.message["text"]
	if("Ass" in message or "ass" in message):
		update.message.reply_text("Its ess for fuck's sake")

def queryHandler(update, context):
	query = update.callback_query.data
	update.callback_query.answer()

	# if "join_giveaway" in query:
	# 	update.message.reply_text("Success")



updater = telegram.ext.Updater(api_key,use_context=True)
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
disp.add_handler(telegram.ext.CommandHandler("myBalance",myWallet))
disp.add_handler(telegram.ext.CommandHandler("yoda",yoda))
disp.add_handler(telegram.ext.CommandHandler("badbot",badbot))
disp.add_handler(telegram.ext.CommandHandler("give",giveaway))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.filters.Filters.text, MessageHandler))
disp.add_handler(telegram.ext.CallbackQueryHandler(queryHandler))

updater.start_polling()
updater.idle()