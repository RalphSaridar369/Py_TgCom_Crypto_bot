from functions.main import *

def givefunction(update, context):
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
