import shelve
#GLOBAL VARIABLES 
HELP = """
		The following commands are available:
		/guide => Give an introduction
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
From token whitelists to presales to launch dates to even NFTs.\n\n
press on that link to get to know more about us: https://t.me/DefiCommuityBot?start"""

ShelfFile = shelve.open('shelf')
ShelfFile['calendar'] = ""
ShelfFile['whitelist_html'] = ""
ShelfFile['calendar_html'] = ""
ShelfFile['presale_html'] = ""
CALENDAR = ShelfFile['calendar']

def setHtmlUrl(value):
	print("Setting Shelf Data Whitelist: ",value)
	ShelfFile['whitelist_html'] = value

def getHtmlUrl():
	print("Getting Shelf Data Whitelist")
	return ShelfFile['whitelist_html']

def setHtmlCalUrl(value):
	print("Setting Shelf Data Calendar: ",value)
	ShelfFile['calendar_html'] = value

def getHtmlCalUrl():
	print("Getting Shelf Data Calendar")
	return ShelfFile['calendar_html']

def setHtmlPreUrl(value):
	print("Setting Shelf Data Presale: ",value)
	ShelfFile['presale_html'] = value

def getHtmlPreUrl():
	print("Getting Shelf Data Presale")
	return ShelfFile['presale_html']