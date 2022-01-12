from functions.main import * 
from functions.giveaway import * 
from functions.globals import * 
from data.About import *
def queryHandler(update, context):
    query = update.callback_query.data.split("-")
    user = update.callback_query.from_user.username
    iduser = update.callback_query.from_user.id
    if(query[1]):
        query = update.callback_query.data.split("-")
        update.callback_query.answer()
        if "join_giveaway" in query[0]:
            f = open("giveaway.txt","r")
            lines = f.readlines()
            if("@"+user not in lines):
                fi = open("giveaway.txt", "a")
                fi.write("\n@"+user)
                fi.close()
            else:
                pass

        elif "chapter" in query[0]:
            choice = int(update.callback_query.data.split("_")[1])
            context.bot.send_message(chat_id=iduser, text=dataAbout[choice-1],
		parse_mode = telegram.ParseMode.HTML)
