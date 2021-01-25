import random

def get_rid_of_errors(msg):
    #language filter
    if msg.content.lower() in ["fuck", "shit"]:
        user = msg.author
        if user.bot == False:
            member = msg.author
            numb = random.randint(1,5)
            if numb == 2:
                await msg.channel.send("Hey " + member.mention + "! Watch your pooping language.")

