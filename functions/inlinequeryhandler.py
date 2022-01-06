from functions.main import *
from functions.globals import * 

def InlineQueryHandler(update, context):
	
	query = update.inline_query.query
	# calendar = getTodayCalendar(update,context,"context")
	# print("Calendar:  "+str(calendar))
	# whitelist = readToday(update,context,"context")
	print("tsting")
	global ONGOING_WHITELIST
	global HTML_DATA_URL
	wlRes = checkIfWhitelistExists()
	# global HTML_CALENDAR_DATA_URL
	#if query == "":
	#	return
	# print("QUERY: "+str(update))
		# chat = context.bot.get_chat()
		# print("CHAT"+str(chat))
	update.inline_query.answer([
	InlineQueryResultArticle(
            id = str(uuid4()),
			title="Ongoing Whitelist",
			input_message_content=InputTextMessageContent(getHtmlUrl(),parse_mode=ParseMode.HTML),
			description="Shows all the ongoing whitelists.",
		),
	# InlineQueryResultArticle(
    #         id = str(uuid4()),
	# 		title="Calendar",
	# 		input_message_content=InputTextMessageContent(calendar,parse_mode=ParseMode.HTML),
	# 		description="Shows calendar for the day"
	# 	),
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
