from functions.main import *

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
