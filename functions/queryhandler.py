from functions.main import * 
from functions.giveaway import * 

def queryHandler(update, context):
    query = update.callback_query.data.split("-")
#     global ALLOWED_TO_JOIN
#     print(ALLOWED_TO_JOIN)
    if(query[1]):
        user = update.callback_query.from_user.username
        # print("DATA: "+update.callback_query.data)
        query = update.callback_query.data.split("-")
        update.callback_query.answer()
        if "join_giveaway" in query[0]:
        #     print(user)
            f = open("giveaway.txt","r")
            lines = f.readlines()
            if("@"+user not in lines):
                fi = open("giveaway.txt", "a")
                fi.write("\n@"+user)
                fi.close()
            else:
                # print("Test")
                pass
