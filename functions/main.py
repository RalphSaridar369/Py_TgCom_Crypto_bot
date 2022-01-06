import requests
import telegram.ext
from telegram import *
from datetime import date
import math
import random
import shelve
from uuid import uuid4
from telegram.utils.helpers import escape_markdown

#GLOBAL VARIABLES
ShelfFile = shelve.open('shelf')
ShelfFile['calendar'] = ""
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
HTML_DATA_URL = None
HTML_CALENDAR_DATA_URL = None
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
		try:
			lines = ShelfFile['whitelist']
		except ValueError:
			if(typeM=="normal"):
				update.message.reply_text("You haven't inserted any whitelists yet")

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

def checkIfWhitelistExists ():
	global HTML_DATA_URL
	if(HTML_DATA_URL == None):
		return "You haven't inserted whitelists yet"
	else:
		return HTML_DATA_URL

def getTodayCalendar(update,context,typeM):
	global CALENDAR
	global HTML_CALENDAR_DATA_URL
	print("Getting calendar")
	today_date = date.today().strftime("%d/%m")
	result=""
	try:
		print(CALENDAR[today_date])
		result = CALENDAR[today_date]
	except:
		result = "You haven't inserted any calendar yet"		
		return result
	if(typeM=="update"):
		update.message.reply_text(result)
	else:
		return HTML_CALENDAR_DATA_URL

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

def help(update, context):
	update.message.reply_text(HELP)

def calendar(update, context):
	
	sender = update.message.from_user.username
	global CALENDAR
	if("=" in update.message.text):
		data = update.message.text.split("=")[1][1::]
		update.message.reply_text("**("+data+"): **\n\n\n"+CALENDAR[data])
	else:
		print("in")
		getTodayCalendar(update, context,"update")

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
