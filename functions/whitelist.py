from functions.main import *
from functions.globals import * 

def whitelist(update, context):

        sender = update.message.from_user.username
        print("SENDER:"+sender)
        if(sender not in ADMINS):
                notAllowed(update,context)
        else:
                print(update.message.text)
                all_options = update.message
                option=[]
                try:
                        option = all_options.text.split(" ")[1]
                except:
                        pass
                if(len(option)<1):
                        readToday(update,context,"normal")
                elif(option=="add"):
                        message = all_options.text.split("=")[1][1::]
                        data = message.split("-")
                        print("data",data)
                        ShelfFile = shelve.open('shelf')
                        for i in data:
                                ShelfFile['whitelist'] += str(i) + '\n'
                        ShelfFile.close()
                        update.message.reply_text("Successfully added")
                elif(option=="read"):
                        readToday(update,context,"normal")
                        pass
                        # ShelfFile = shelve.open('shelf')
                        # lines = ShelfFile['whitelist']
                        # #try:
                        # #     lines = lines.replace('\n', '')
                        # #except ValueError:
                        # #     pass
                        # print('test')
                        # message = "Whitelists: \n\n"
                        # message += lines
                        # update.message.reply_text(message)
                elif(option=="remove"):
                        ShelfFile = shelve.open('shelf')
                        ShelfFile['whitelist'] = ''
                        ShelfFile.close()
                        update.message.reply_text("Successfully Removed")
                else:
                        update.message.reply_text("Please choose either: add, read or remove")

