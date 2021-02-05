import discord
from discord.utils import get
from discord import Member
from discord.ext import commands
import asyncio


client = discord.Client()
#mod commands

@client.event
async def kick(msg):
    
    member = msg.author
    if discord.utils.get(member.roles, name="Head Admin") is None:
        await msg.channel.send("You don't have permission to kick ")
        
    else:
        for user in msg.mentions:
            await user.kick()
            await msg.channel.send(str(user) + " has been kicked")
        
@client.event
async def ban(msg):
    
    member = msg.author
    if discord.utils.get(member.roles, name="Head Admin") is None:
        for user in msg.mentions:
            
            await msg.channel.send("You dont have permission to ban " + str(user))
    else:
        for user in msg.mentions:
            
            await user.ban()
            await msg.channel.send(str(user) + " has been banned")
        
async def banlist(msg):
    guild = msg.guild
    bans = await guild.bans()
    for ban in bans:
        await msg.channel.send("Name - `" + str(ban.user.name) + "`, ID - `" + str(ban.user.id) + "`")



@client.event
async def mute(msg):
    
    member = msg.author
    if discord.utils.get(member.roles, name="Head Admin") is None:
        for user in msg.mentions:
            
            await msg.channel.send("You dont have permission to mute " + str(user))
        
    else:
        for user in msg.mentions:
            
            role = discord.utils.get(msg.guild.roles, name='Muted')
            await user.add_roles(role)
            await user.edit(voice_channel=None)
            await msg.channel.send(str(user) + " has been muted")

async def unmute(msg):
    
    member = msg.author
    if discord.utils.get(member.roles, name="Head Admin") is None:
        for user in msg.mentions:
            
            await msg.channel.send("You dont have permission to unmute " + str(user))
    else:
        for user in msg.mentions:
            
            role = discord.utils.get(msg.guild.roles, name='Muted')
            await user.remove_roles(role)
            await msg.channel.send(str(user) + " has been unmuted")

async def nick(msg):
    
    
    if msg.content.split(" ")[1] == "reset":
        for user in msg.mentions:
            nick = user.name
            await user.edit(nick=nick)
            await msg.channel.send("Users nick has been reset.")
    else:
        nick = msg.content.split(" ")[2:]
        actualnick = ''.join(nick)
        for user in msg.mentions:
            await user.edit(nick=actualnick)
            await msg.channel.send(str(user) + "'s nick has been changed.")

async def warn(msg):
    
    warnin = msg.content.split(" ")[2:]
    warning = ''.join(warnin)
    for user in msg.mentions:
        await user.send("You have been warned on " + str(user.guild.name) + " for " + str(warning))
        await msg.channel.send(str(user) + " has been warned.")
        

async def shutdown(client, msg):
    
    if msg.author.id == 698707989531459595:
        await msg.channel.send(msg.author.mention + ", how could you do this?", delete_after=0.5) 
        await asyncio.sleep(1)
        await msg.channel.send("Shutting down...", delete_after=0.2)
        await asyncio.sleep(0.5)
        await msg.delete()
        await client.get_channel(801262872955977729).send("Bot has been shutdown!")
        await client.logout()
        print ("Bot shutdown")

async def yeet(msg):
    if discord.utils.get(msg.author.roles, name="Head Admin") is None:
        await msg.channel.send("You can't do that.")
    else:
        if msg.mentions:
            for user in msg.mentions:
                me = []
                async for m in msg.channel.history():
        
                    if m.author == user:
                        me.append(m)
                        await msg.channel.delete_messages(me)
                        await msg.channel.send("All messages by " + user.mention + " have been deleted.")
        else:
            llimit = msg.content.split(" ")[1]
            await msg.channel.purge(limit=int(llimit))
            await msg.channel.send("Chat cleared by " + msg.author.display_name, delete_after=2.0) 

            
        



async def addrole(msg):
    
    member = msg.author
    
    rolemsg = msg.content.split(" ")[2]
    if rolemsg == "nsfw":
        role = get(msg.guild.roles , name='nsfw')
        if role in member.roles:
            await msg.channel.send(member.mention + " already has " + str(role))
        else:
            for user in msg.mentions:

                await user.add_roles(role)
                await msg.channel.send(str(role) + " has been added to " + user.mention)
    if rolemsg == "wet":
        role = get(msg.guild.roles , name='wet')
        if role in member.roles:
            await msg.channel.send(member.mention + " already has " + str(role))
        else:
            for user in msg.mentions:

                await user.add_roles(role)
                await msg.channel.send(str(role) + " has been added to " + user.mention)
    if rolemsg == "bedwars player":
        role = get(msg.guild.roles , name='bedwars player')
        if role in member.roles:
            await msg.channel.send(member.mention + " already has " + str(role))
        else:
            for user in msg.mentions:

                await user.add_roles(role)
                await msg.channel.send(str(role) + " has been added to " + user.mention)
    if rolemsg == "#jellyforowner2021":
        role = get(msg.guild.roles , name='#jellyforowner2021')
        if role in member.roles:
            await msg.channel.send(member.mention + " already has " + str(role))
        else:
            for user in msg.mentions:

                await user.add_roles(role)
                await msg.channel.send(str(role) + " has been added to " + user.mention)
    if rolemsg == "british":
        role = get(msg.guild.roles , name='british')
        if role in member.roles:
            await msg.channel.send(member.mention + " already has " + str(role))
        else:
            for user in msg.mentions:

                await user.add_roles(role)
                await msg.channel.send(str(role) + " has been added to " + user.mention)
    if rolemsg == "child stabber":
        role = get(msg.guild.roles , name='child stabber')
        if role in member.roles:
            await msg.channel.send(member.mention + " already has " + str(role))
        else:
            for user in msg.mentions:

                await user.add_roles(role)
                await msg.channel.send(str(role) + " has been added to " + user.mention)  
    if rolemsg == "duck":
        role = get(msg.guild.roles , name='duck')
        if role in member.roles:
            await msg.channel.send(member.mention + " already has " + str(role))
        else:
            for user in msg.mentions:

                await user.add_roles(role)
                await msg.channel.send(str(role) + " has been added to " + user.mention)
    if rolemsg == "i am a cake":
        role = get(msg.guild.roles , name='i am a cake')
        if role in member.roles:
            await msg.channel.send(member.mention + " already has " + str(role))
        else:
            for user in msg.mentions:

                await user.add_roles(role)
                await msg.channel.send(str(role) + " has been added to " + user.mention)
    if rolemsg == "waffle":
        role = get(msg.guild.roles , name='waffle')
        if role in member.roles:
            await msg.channel.send(member.mention + " already has " + str(role))
        else:
            for user in msg.mentions:

                await user.add_roles(role)
                await msg.channel.send(str(role) + " has been added to " + user.mention)
    if rolemsg == "Member":
        role = get(msg.guild.roles , name='Member')
        if role in member.roles:
            await msg.channel.send(member.mention + " already has " + str(role))
        else:
            for user in msg.mentions:

                await user.add_roles(role)
                await msg.channel.send(str(role) + " has been added to " + user.mention)
    if rolemsg == "hi im a bot":
        role = get(msg.guild.roles , name='hi im a bot')
        if role in member.roles:
            await msg.channel.send(member.mention + " already has " + str(role))
        else:
            for user in msg.mentions:

                await user.add_roles(role)
                await msg.channel.send(str(role) + " has been added to " + user.mention)
    if rolemsg == "Administrator":
        role = get(msg.guild.roles , name='Administrator')
        if role in member.roles:
            await msg.channel.send(member.mention + " already has " + str(role))
        else:
            for user in msg.mentions:

                await user.add_roles(role)
                await msg.channel.send(str(role) + " has been added to " + user.mention)
    if rolemsg == "Muted":
        role = get(msg.guild.roles , name='Muted')
        if role in member.roles:
            await msg.channel.send(member.mention + " already has " + str(role))
        else:
            for user in msg.mentions:

                await user.add_roles(role)
                await msg.channel.send(str(role) + " has been added to " + user.mention)
    
    

async def delrole(msg):
    
    member = msg.author
    
    rolemsg = msg.content.split(" ")[2]
    if rolemsg == "nsfw":
        role = get(msg.guild.roles , name='nsfw')
        if role in member.roles == None:
            await msg.channel.send(member.mention + " doesn't have " + str(role))
        else:
            for user in msg.mentions:

                await user.remove_roles(role)
                await msg.channel.send(str(role) + " has been removed from " + user.mention)
    if rolemsg == "wet":
        role = get(msg.guild.roles , name='wet')
        if role in member.roles == None:
            await msg.channel.send(member.mention + " doesn't have " + str(role))
        else:
            for user in msg.mentions:

                await user.remove_roles(role)
                await msg.channel.send(str(role) + " has been removed from " + user.mention)
    if rolemsg == "bedwars player":
        role = get(msg.guild.roles , name='bedwars player')
        if role in member.roles == None:
            await msg.channel.send(member.mention + " doesn't have " + str(role))
        else:
            for user in msg.mentions:

                await user.remove_roles(role)
                await msg.channel.send(str(role) + " has been removed from " + user.mention)
    if rolemsg == "#jellyforowner2021":
        role = get(msg.guild.roles , name='#jellyforowner2021')
        if role in member.roles == None:
            await msg.channel.send(member.mention + " doesn't have " + str(role))
        else:
            for user in msg.mentions:

                await user.remove_roles(role)
                await msg.channel.send(str(role) + " has been removed from " + user.mention)
    if rolemsg == "british":
        role = get(msg.guild.roles , name='british')
        if role in member.roles == None:
            await msg.channel.send(member.mention + " doesn't have " + str(role))
        else:
            for user in msg.mentions:

                await user.remove_roles(role)
                await msg.channel.send(str(role) + " has been removed from " + user.mention)
    if rolemsg == "child stabber":
        role = get(msg.guild.roles , name='child stabber')
        if role in member.roles == None:
            await msg.channel.send(member.mention + " doesn't have " + str(role))
        else:
            for user in msg.mentions:

                await user.remove_roles(role)
                await msg.channel.send(str(role) + " has been removed from " + user.mention)  
    if rolemsg == "duck":
        role = get(msg.guild.roles , name='duck')
        if role in member.roles == None:
            await msg.channel.send(member.mention + " doesn't have " + str(role))
        else:
            for user in msg.mentions:

                await user.remove_roles(role)
                await msg.channel.send(str(role) + " has been removed from " + user.mention)
    if rolemsg == "i am a cake":
        role = get(msg.guild.roles , name='i am a cake')
        if role in member.roles == None:
            await msg.channel.send(member.mention + " doesn't have " + str(role))
        else:
            for user in msg.mentions:

                await user.remove_roles(role)
                await msg.channel.send(str(role) + " has been removed from " + user.mention)
    if rolemsg == "waffle":
        role = get(msg.guild.roles , name='waffle')
        if role in member.roles == None:
            await msg.channel.send(member.mention + " doesn't have " + str(role))
        else:
            for user in msg.mentions:

                await user.remove_roles(role)
                await msg.channel.send(str(role) + " has been removed from " + user.mention)
    if rolemsg == "Member":
        role = get(msg.guild.roles , name='Member')
        if role in member.roles == None:
            await msg.channel.send(member.mention + " doesn't have " + str(role))
        else:
            for user in msg.mentions:

                await user.remove_roles(role)
                await msg.channel.send(str(role) + " has been removed from " + user.mention)
    if rolemsg == "hi im a bot":
        role = get(msg.guild.roles , name='hi im a bot')
        if role in member.roles == None:
            await msg.channel.send(member.mention + " doesn't have " + str(role))
        else:
            for user in msg.mentions:

                await user.remove_roles(role)
                await msg.channel.send(str(role) + " has been removed from " + user.mention)
    if rolemsg == "Administrator":
        role = get(msg.guild.roles , name='Administrator')
        if role in member.roles == None:
            await msg.channel.send(member.mention + " doesn't have " + str(role))
        else:
            for user in msg.mentions:

                await user.remove_roles(role)
                await msg.channel.send(str(role) + " has been removed from " + user.mention)
    if rolemsg == "Muted":
        role = get(msg.guild.roles , name='Muted')
        if role in member.roles == None:
            await msg.channel.send(member.mention + " doesn't have " + str(role))
        else:
            for user in msg.mentions:

                await user.remove_roles(role)
                await msg.channel.send(str(role) + " has been removed from " + user.mention)