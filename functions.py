import requests
import telegram.ext
from telegram import *
from datetime import date
import math
import random
import shelve
from uuid import uuid4
from telegram.utils.helpers import escape_markdown
from uuid import uuid4

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
		/cal = dd/mm => gets all whitelists on a specific date
		/cal => gets today's whitelists
		/meme => sends a meme
	"""
CHAT_ID = -1001775758804
GIVEAWAY_ID = 0
GIVEAWAY_RUNNING= False
ONGOING_WHITELIST = ""
ADMINS = ["Zhee_Conan","thebastardmak","cryptolima","watwatian","FaridFlintstone","vengefulsaxophone"]
SUPER_ADMIN = ["cryptolima"]
COIN_FLIP = ["Head","Tails"]
WINNERS = 0
ABOUT_US_MESSAGE = """** Lebanese DeFi **\n\nWelcome to the group

We are working on building a community

La ne2dar kelna na3mol profits w nse3ed ba3ed at the end of the day

From token whitelists to presales to launch dates to even NFTs"""

#FUNCTIONS
def notAllowed(update,context):
	message = ["Not allowed habibo","Enssss","Jareba ba3ed marra barken btezbat"]
	update.message.reply_text(message[random.randint(0,len(message)-1)])

def start(update, context):
	update.message.reply_text("Hello! Welcome to Lebanese DeFi! Let's make some bucks baby...")

def meme(update,context):
	chatid = update['message']['chat']['id']
	page = requests.get("https://meme-api.herokuapp.com/gimme")
	res = page.json()
	context.bot.sendPhoto(chat_id=chatid, photo=res['url'], caption=res['title'])

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
		option=[]
		try:
			option = all_options.text.split(" ")[1]
		except:
			pass
		if(len(option)<1):
			readToday(update,context,"normal")
		elif(option=="add"):
			message = all_options.text.split("=")[1][1::]
			data = message.split("-")
			print("data",data)
			ShelfFile = shelve.open('shelf')
			for i in data:
				ShelfFile['whitelist'] += str(i) + '\n'
			ShelfFile.close()
			update.message.reply_text("Successfully added")
		elif(option=="read"):
			readToday(update,context,"normal")
			# ShelfFile = shelve.open('shelf')
			# lines = ShelfFile['whitelist']
			# #try:
			# #	lines = lines.replace('\n', '')
			# #except ValueError:
			# #	pass
			# print('test')
			# message = "Whitelists: \n\n"
			# message += lines
			# update.message.reply_text(message)
		elif(option=="remove"):
			ShelfFile = shelve.open('shelf')
			ShelfFile['whitelist'] = ''
			ShelfFile.close()
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

def readToday(update,context,typeM):
		ShelfFile = shelve.open('shelf')
		lines = ShelfFile['whitelist']
		#try:
		#	lines = lines.replace('\n', '')
		#except ValueError:
		#	pass
		message = "Whitelists: \n\n"
		message += lines
		if(typeM == "normal"):
			update.message.reply_text(message)
		else:
			return message

def getTodayCalendar(update,context,typeM):
	global CALENDAR
	print("Getting calendar")
	today_date = date.today().strftime("%d/%m")
	result=""
	try:
		print(CALENDAR[today_date])
		result = CALENDAR[today_date]
	except:
		result = "You haven't inserted any calendar yet"
		print("Error")
	if(typeM=="update"):
		update.message.reply_text(result)
	else:
		return result

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
	print("callback")

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

def InlineQueryHandler(update, context):
	
	query = update.inline_query.query
	calendar = getTodayCalendar(update,context,"context")
	# whitelist = readToday(update,context,"context")
	global ONGOING_WHITELIST
	ShelfFile = shelve.open('shelf')
	ONGOING_WHITELIST = ShelfFile['whitelist']
	ShelfFile.close()
	#if query == "":
	#	return
	# print("QUERY: "+str(update))
		# chat = context.bot.get_chat()
		# print("CHAT"+str(chat))
	update.inline_query.answer([
	InlineQueryResultArticle(
            id = str(uuid4()),
			title="Ongoing Whitelist",
			input_message_content=InputTextMessageContent(ONGOING_WHITELIST),
			description="Shows all the ongoing whitelists.",
		),
		InlineQueryResultArticle(
            id = str(uuid4()),
			title="Calendar",
			input_message_content=InputTextMessageContent(str(calendar)),
			description="Shows calendar for the day"
		),
	])
	


# def chosenInline(update,context):
# 	print("+\n+")
# 	choice = update.chosen_inline_result.result_id
# 	chat_id = update.chosen_inline_result.from_user.id
# 	if(choice==1):
# 		context.bot.send_message(text="wl", chat_id=chat_id)
# 	else:
# 		x  = getTodayCalendar(update,context,"context")
# 		context.bot.send_message(text=x, chat_id=chat_id)

def queryHandler(update, context):
	global ALLOWED_TO_JOIN
	if(ALLOWED_TO_JOIN):
		user = update.callback_query.from_user.username
		print("DATA: "+update.callback_query.data)
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
		else:
			print("Test")

def MessageHandler(update, context):
	global CALENDAR
	global ADMINS
	sender = update.message.from_user.username
	message = update.message["text"]
	print(message)
	if("@BscFetcherDevBot" in message):
		if("cal" in message):
			print(update.message.chat.id)
			# x = getTodayCalendar(update,context,"context")
			# context.bot.send_message(chat_id=update.effective_chat.id,text=x)
	elif("Ass" in message or "ass" in message):
		update.message.reply_text("Its ess for fuck's sake")
	elif("🔱 TOKEN CALANDER" in message ):
		# here it should be shelf
		print("Should add the list")
		print(message)
		today_date = date.today().strftime("%d/%m")
		ShelfFile = shelve.open('shelf')
		#add the shelf here
		CALENDAR[today_date] = message
		ShelfFile['calendar'][today_date] = CALENDAR[today_date]
		ShelfFile.close()
		update.message.reply_text("I added it to our list, if you want to check, write /cal read")
	elif("❄️☃️Ongoing whitelist competitions ☃️❄️" in message):
		global ONGOING_WHITELIST
		ONGOING_WHITELIST = message
		ShelfFile = shelve.open('shelf')
		#add the shelf here
		ShelfFile['whitelist'] = message
		ShelfFile.close()
		update.message.reply_text("I added it to our ongoing whitelist")


def help(update, context):
	update.message.reply_text(HELP)

def calendar(update, context):
	
	sender = update.message.from_user.username
	# if(sender not in ADMINS):
	# 	notAllowed(update,context)
	#else:
	global CALENDAR
	#all_options = update.message
	#option = all_options.text.split(" ")[1]
	# if(option ==""):
	# 	today_date = date.today().strftime("%d/%m")
	# 	data = update.message.text.split("=")[1][1::]
	# 	update.message.reply_text(CALENDAR[data])
	# elif(option == "today"):
	# 	today_date = date.today().strftime("%d/%m")
	# 	data = update.message.text.split("=")[1]
	# 	ShelfFile = shelve.open('shelf')
	# 	CALENDAR[today_date] = data
	# 	ShelfFile['calendar'][today_date] = CALENDAR[today_date]
	# 	ShelfFile.close()
	#   update.message.reply_text("Successfully added")
	if("=" in update.message.text):
		data = update.message.text.split("=")[1][1::]
		update.message.reply_text("**("+data+"): **\n\n\n"+CALENDAR[data])
	else:
		print("in")
		getTodayCalendar(update, context,"update")
		# today_date = date.today().strftime("%d/%m")
		# update.message.reply_text("**TODAY's CALENDAR: **\n\n\n"+CALENDAR[today_date])

def joke(update, context):
	data = ["Omak 3andi","I know your momma and, she knows me. You better believe it.","اعرف اين امك ايها الحقير"]
	choice = random.randint(0,1)
	if(choice==0):
		jokeChoice = random.randint(0,2)
		update.message.reply_text(data[jokeChoice])
	else: 
		page = requests.get("https://api.yomomma.info/",headers={"Accept":"application/json"})
		res= page.json()
		joke = res["joke"]
		update.message.reply_text(joke)

def adminpanel(update,context):
		# button = [
		# [InlineKeyboardButton("Join",callback_data="test")],
		# [InlineKeyboardButton("Join",callback_data="test")],
		# [InlineKeyboardButton("Join",callback_data="test")],
		# [InlineKeyboardButton("Join",callback_data="test")],
		# [InlineKeyboardButton("Join",callback_data="test")],
		# [InlineKeyboardButton("Join",callback_data="test")],
		# [InlineKeyboardButton("Join",callback_data="test")],
		# [InlineKeyboardButton("Join",callback_data="test")],
		# [InlineKeyboardButton("Join",callback_data="test")],]
		# sent = context.bot.send_message(chat_id=update.effective_chat.id, text="Admin Panel",
		# reply_markup=InlineKeyboardMarkup(button))
		"""
		Start function. Displayed whenever the /start command is called.
		This function sets the language of the bot.
		"""
		# Create buttons to slect language:
		keyboard = [[KeyboardButton("/cal",callback_data="today_calendar"),KeyboardButton("/wl read",callback_data="whitelists")]]

		# Create initial message:
		message = "Please choose one of the options below"
		reply_markup = ReplyKeyboardMarkup(keyboard,one_time_keyboard=False,resize_keyboard=True)
		update.message.reply_text(message, reply_markup=reply_markup)
