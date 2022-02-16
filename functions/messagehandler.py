from functions.main import *
from functions.globals import * 

def MessageHandler(update, context):
	global CALENDAR
	global ADMINS
	sender = update.message.from_user.username
	message = update.message["text"]
	# print(message)
	# print(sender)
	if("@BscFetcherDevBot" in message):
		if("cal" in message):
			pass
	if("🔱 TOKEN CALANDER" in message ):
		# here it should be shelf
		# print(message)
		today_date = date.today().strftime("%d/%m")
		ShelfFile = shelve.open('shelf')
		#add the shelf here
		CALENDAR[today_date] = message
		ShelfFile['calendar'][today_date] = CALENDAR[today_date]
		ShelfFile.close()
		update.message.reply_text("I added it to our list, if you want to check, write /cal read")
	if("Ongoing whitelist competitions:" in message or "Tracked Projects" in message or "List of Presale and Launch:" in message):
		if("Ongoing whitelist competitions:" in message):
			
			whitelists = update.message.text.split('\n')[1::]
			string = "whitelist Ongoing competitions:\n\n\n"
			count = 0
			countLines = 0
			for i,n in enumerate(whitelists):
				if(("-") in n):
					url = n.split("-")[0]
					date = n.split("-")
					string += "<a href='{}'>{}</a>  {}".format(update.message.entities[i-countLines+1].url,url,date[1])+"\n"
				else:
					countLines +=1   
			### shelf doesnt work for html parse
			# ShelfFile = shelve.open('shelf')
			#add the shelf here
			# ShelfFile['ongoingwhitelist'] = string
			# ShelfFile.close()
			f = open("html.txt","w")
			f.write(string)
			setHtmlUrl(string)
			f.close()
			update.message.reply_text("I added it to our ongoing whitelist")
		if("Tracked Projects:" in message):
			# print(update.message)
			trackedprojects = update.message.text.split('Binance Smart Chain:\n')
			string = trackedprojects[0].replace("Tracked Projects","Projects Tracked")
			for i,n in enumerate(trackedprojects[1].split('members')[:len(trackedprojects[1].split('members'))-1:]):
				n = n + " members"
				url = n.split("-")[0]
				date = n.split("-")[1]
				string += "<a href='{}'>{}</a>  {}".format(update.message.entities[i+2].url,url,date)
			setHtmlCalUrl(string)
			update.message.reply_text("I added today's calendar")
   
		if("List of Presale and Launch:" in message):
			presaleAndLaunches = update.message.text.split('List of Presale and Launch:')[1]
			allPresales = presaleAndLaunches.split('@')
			# print("inside",allPresales)
			# print("update message:",update.message)
			string = "List of Presale and launch:\n"
			for i,n in enumerate(allPresales):
				# print(i,n)
				url = n
				href=""
				if(update.message.entities[i+1].url == None):
					href=""
				else:
					href=update.message.entities[i+1].url
				string += "<a href='{}'>{}</a>".format(href,"@"+url)
				# print("ITEM",n)
			print("END RESULT: ",string)
			print("ENTITIES: ",update.message)
			setHtmlPreUrl(string)
			update.message.reply_text("I added today's presale and launch list")
