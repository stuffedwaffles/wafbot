#language filter
    if "fuck" in msg.content.lower() or "shit" in msg.content.lower() or "damn" in msg.content.lower() or "bitch" in msg.content.lower():
        user = msg.author
        if user.bot == False:
            member = msg.author
            numb = random.randint(1,5)
            if numb == 2:
                await msg.channel.send("Hey " + member.mention + "! Watch your fucking language.")