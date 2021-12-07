import requests
import telegram.ext
from telegram import *
from datetime import date
import random
import shelve
#GLOBAL VARIABLES
ShelfFile = shelve.open('shelf')
CALENDAR = ShelfFile['calendar']
ShelfFile.close()
HELP = """
		The following commands are available:
		/balance => Gives balance of community's wallet
		/about => About Us
		/coinflip => Head or Tails
		/ntek => for ntek purposes
		/joke => sends a Yo mama joke
		/mybalance + hash => sends your own wallet balance
		/pumpit => to pump it up
		/badbot => slap the bot
		/wl add = etc 123-etc 24 => adds etc 123 and etc 24 to the list 
		/wl read => reads whitelist list 
		/wl remove => removes from the list 
		/give name 2 => creates a giveaway with num of winners = 2
		/givestop => stops current giveaway
		/cal today = data => sets whitelist calendar for a specific date
		/cal read = 06/12 => gets all whitelists on a specific date
	"""
CHAT_ID = -1001775758804
GIVEAWAY_ID = 0
GIVEAWAY_RUNNING= False
ADMINS = ["thebastardmak","cryptolima","watwatian","FaridFlintstone","vengefulsaxophone"]
COIN_FLIP = ["Head","Tails"]
WINNERS = 0
ABOUT_US_MESSAGE = """** Lebanese DeFi **\n\nWelcome to the group

We are working on building a community

La ne2dar kelna na3mol profits w nse3ed ba3ed at the end of the day

From token whitelists to presales  to launch dates to even NFTs"""

#FUNCTIONS
def notAllowed(update,context):
	message = ["Not allowed habibo","Enssss","Jareba ba3ed marra barken btezbat"]
	update.message.reply_text(message[random.randint(0,len(message)-1)])

def start(update, context):
	update.message.reply_text("Hello! Welcome to Lebanese DeFi!")

def badbot(update, context):
	arr = ["Sorry :(","Won't happen again","My bad","Please don't hurt my family"]
	update.message.reply_text(arr[random.randint(0,len(arr)-1)])

def whitelist(update, context):
	sender = update.message.from_user.username
	print("SENDER:"+sender)
	if(sender not in ADMINS):
		notAllowed(update,context)
	else:
		print(update.message.text)
		all_options = update.message
		option = all_options.text.split(" ")[1]
		if(option=="add"):
			message = all_options.text.split("=")[1][1::]
			data = message.split("-")
			print("data",data)
			f = open("whitelist.txt","a")
			for i in data:
				f.write(i+"\n")
			f.close()
			update.message.reply_text("Successfully added")
		elif(option=="read"):
			f = open("whitelist.txt","r")
			lines = f.readlines()
			try:
				while True:
					lines.remove("\n")
			except ValueError:
				pass
			message = "Whitelists: \n\n"
			for i in lines:
				message+=i
			update.message.reply_text(message)
		elif(option=="remove"):
			f = open("whitelist.txt","w")
			f.write("")
			f.close()
			update.message.reply_text("Successfully Removed")
		else:
			update.message.reply_text("Please choose either: add, read or remove")

def myWallet(update, context):

	message = update.message["text"]
	hex = message.split(" ")[1]

	page = requests.get("https://api.bscscan.com/api?module=account&action=balance&address="+hex+"&apikey=T7YH7MHHQTPEB25EVTQH5Z7R5H1QK1KVXT")

	res = page.json()
	print(res)
	print("{:.18f}".format(float(res["result"])))
	sum = round(float(res['result'])/math.pow(10,18),2)
	update.message.reply_text("**Your Balance:**\n"+str(sum)+" BNB")

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
	update.message.reply_text("**Community Balance:**\n"+str("{0:.2f}".format(float(res['result'])/math.pow(10,18)))+" BNB")

def callback():
	print("test")

def giveaway(update, context):
	global GIVEAWAY_RUNNING
	global ALLOWED_TO_JOIN

	print("TEST")
	print(GIVEAWAY_RUNNING)
	sender = update.message.from_user.username
	print("SENDER:"+sender)
	if(sender not in ADMINS):
		notAllowed(update,context)
	elif(GIVEAWAY_RUNNING==True):
		print("yes")
		update.message.reply_text("Please run slash stopgive before starting a new giveaway")
	else:
		global WINNERS
		global ALLOWED_TO_JOIN
		GIVEAWAY_RUNNING = True
		ALLOWED_TO_JOIN = True
		message = update.message["text"]
		#print("MESSAGE: ",message)
		giveawayName = message.split(" ")[1]
		winnersLn = int(message.split(" ")[2])
		WINNERS = winnersLn
		#participantsLn = int(message.split(" ")[2])
		#print("Test")
		button = [[InlineKeyboardButton("Join",callback_data="join_giveaway"+"-"+update.message.from_user.first_name+"")]]
		sent = context.bot.send_message(chat_id=update.effective_chat.id, text="Giveaway "+giveawayName+"\n\n\nNumber of Winners: "+str(winnersLn),
		reply_markup=InlineKeyboardMarkup(button))

def stopGiveaway(update, context):
	
	sender = update.message.from_user.username
	print("SENDER:"+sender)
	if(sender not in ADMINS):
		notAllowed(update,context)
	else:
		global ALLOWED_TO_JOIN
		global WINNERS 
		global CHAT_ID
		global GIVEAWAY_RUNNING
		GIVEAWAY_RUNNING=False
		ALLOWED_TO_JOIN=False
		
		# context.bot.deleteMessage (message_id = must_delete.message_id,
        # chat_id = CHAT_ID)
		f = open("giveaway.txt", "r")
		participants=[]
		for i in f.readlines():
			participants.append(i)
		participants=participants[1::]
		print(participants)	
		try:
			while True:
				participants.remove("\n")
		except ValueError:
			pass
		if(len(participants)<=WINNERS):
			winners=""	
			for i,n in enumerate(participants):
				print("i: ",i)
				winners+=n
			update.message.reply_text("Congrats:\n\n"+winners)
		else:
			winners=""
			for i in range(WINNERS):
				choice = random.randint(0,len(participants)-1)
				winners+=participants[choice]
				participants.remove(participants[choice])
			update.message.reply_text("Congrats:\n\n"+winners)
			
		f.close()
		f  = open("giveaway.txt", "w")
		f.write("participants:\n")

def queryHandler(update, context):
	global ALLOWED_TO_JOIN
	if(ALLOWED_TO_JOIN):
		user = update.callback_query.from_user.username
		query = update.callback_query.data.split("-")
		update.callback_query.answer()
		if "join_giveaway" in query[0]:
			print(user)
			f = open("giveaway.txt","r")
			lines = f.readlines()
			if("@"+user not in lines):
				fi = open("giveaway.txt", "a")
				fi.write("\n@"+user)
				fi.close()
	# 	update.message.reply_text("Success")

def MessageHandler(update, context):
	message = update.message["text"]
	if("Ass" in message or "ass" in message):
		update.message.reply_text("Its ess for fuck's sake")

def help(update, context):
	update.message.reply_text(HELP)

def calendar(update, context):
	
	sender = update.message.from_user.username
	if(sender not in ADMINS):
		notAllowed(update,context)
	else:
		global CALENDAR
		all_options = update.message
		option = all_options.text.split(" ")[1]
		print(option)
		if(option == "today"):
			print(456)
			today_date = date.today().strftime("%d/%m")
			data = update.message.text.split("=")[1]
			ShelfFile = shelve.open('shelf')
			CALENDAR[today_date] = data
			ShelfFile['calendar'][today_date] = CALENDAR[today_date]
			ShelfFile.close()
			update.message.reply_text("Successfully added")
		elif(option == "read"):
			print(123)
			data = update.message.text.split("=")[1][1::]
			print(data)
			update.message.reply_text(CALENDAR[data])

def joke(update, context):
	#page = requests.get("https://v2.jokeapi.dev/joke/Dark,Pun?blacklistFlags=nsfw,religious,political,racist,sexist,explicit",headers={"Accept":"application/json"})
	page = requests.get("https://api.yomomma.info/",headers={"Accept":"application/json"})
	res= page.json()
	#joke = res["setup"]+" "+res["delivery"]
	joke = res["joke"]
	update.message.reply_text(joke)
