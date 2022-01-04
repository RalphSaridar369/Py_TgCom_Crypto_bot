def MessageHandler(update, context):
	global CALENDAR
	global ADMINS
	sender = update.message.from_user.username
	message = update.message["text"]
	print(sender)
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
	elif("Ongoing whitelist competitions:" in message or "Tracked Projects" in message):
		if("Ongoing whitelist competitions:" in message):
			whitelists = update.message.text.split('\n')[3::]
			string = "Ongoing whitelist competitions:\n\n\n"
			for i,n in enumerate(whitelists):
				url = n.split("-")[0]
				date = n.split("-")[1]
				string += "<a href='{}'>{}</a>  {}".format(update.message.entities[i].url,url,date)+"\n"
			global ONGOING_WHITELIST
			global HTML_DATA_URL
			ONGOING_WHITELIST = message
			### shelf doesnt work for html parse
			# ShelfFile = shelve.open('shelf')
			#add the shelf here
			# ShelfFile['ongoingwhitelist'] = string
			# ShelfFile.close()
			f = open("html.txt","w")
			f.write(string)
			HTML_DATA_URL = string
			f.close()
			update.message.reply_text("I added it to our ongoing whitelist")
		elif("Tracked Projects" in message):
			trackedprojects = update.message.text.split('Binance Smart Chain:\n')
			string = trackedprojects[0]
			for i,n in enumerate(trackedprojects[1].split('members')[:len(trackedprojects[1].split('members'))-1:]):
				# print(len(trackedprojects[1].split('members')[::]))
				# if(i<2):
				# 	continue
				# print(update.message)
				n = n + " members"
				print(n)
				print(update.message.entities[i+2].url)
				url = n.split("-")[0]
				print(url)
				date = n.split("-")[1]
				string += "<a href='{}'>{}</a>  {}".format(update.message.entities[i+2].url,url,date)
			# global ONGOING_WHITELIST
			global HTML_CALENDAR_DATA_URL
			f = open("calendarhtml.txt","w")
			f.write(string)
			HTML_CALENDAR_DATA_URL = string
			f.close()
			update.message.reply_text("I added today's calendar")
	elif("testing" in message):
		f = open("html.txt","r")
		update.message.reply_text(''.join(f.readlines()),parse_mode=ParseMode.HTML)
		f.close()
