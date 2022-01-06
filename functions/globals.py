#GLOBAL VARIABLES 
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

def setHtmlUrl(value):
    global HTML_DATA_URL
    HTML_DATA_URL = value

def getHtmlUrl():
    global HTML_DATA_URL
    return str(HTML_DATA_URL)