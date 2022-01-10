from functions.main import *
from functions.globals import * 

def MessageHandler(update, context):
	global CALENDAR
	global ADMINS
	sender = update.message.from_user.username
	message = update.message["text"]
	print(message)
	# print(sender)
	if("@BscFetcherDevBot" in message):
		if("cal" in message):
			pass
			# print(update.message.chat.id)
			# x = getTodayCalendar(update,context,"context")
			# context.bot.send_message(chat_id=update.effective_chat.id,text=x)
	if("Ass" in message or "ass" in message):
		update.message.reply_text("Its ess for fuck's sake")
	if("🔱 TOKEN CALANDER" in message ):
		# here it should be shelf
		# print("Should add the list")
		# print(message)
		today_date = date.today().strftime("%d/%m")
		ShelfFile = shelve.open('shelf')
		#add the shelf here
		CALENDAR[today_date] = message
		ShelfFile['calendar'][today_date] = CALENDAR[today_date]
		ShelfFile.close()
		update.message.reply_text("I added it to our list, if you want to check, write /cal read")
	if("Ongoing whitelist competitions:" in message or "Tracked Projects" in message):
		if("Ongoing whitelist competitions:" in message):
			
			whitelists = update.message.text.split('\n')[1::]
			string = "whitelist Ongoing competitions:\n\n\n"
			count = 0
			countLines = 0
			# for i,n in enumerate(whitelists):
			# 	print(update.message.entities[i])
			# 	if(update.message.entities[i].url == None):
			# 		count += 1
			# 	else:
			# 		break
			# print(count)
			for i,n in enumerate(whitelists):
				if(("-") in n):
					# print("ITEM: ",n," ",i)
					# print(update.message.entities[i-2].url)
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
			trackedprojects = update.message.text.split('Binance Smart Chain:\n')
			string = trackedprojects[0].replace("Tracked Projects","Projects Tracked")
			for i,n in enumerate(trackedprojects[1].split('members')[:len(trackedprojects[1].split('members'))-1:]):
				# print(len(trackedprojects[1].split('members')[::]))
				# if(i<2):
				# 	continue
				# print(update.message)
				n = n + " members"
				# print(n)
				# print(update.message.entities[i+2].url)
				url = n.split("-")[0]
				# print(url)
				date = n.split("-")[1]
				string += "<a href='{}'>{}</a>  {}".format(update.message.entities[i+2].url,url,date)
			setHtmlCalUrl(string)
			# global ONGOING_WHITELIST
			update.message.reply_text("I added today's calendar")
