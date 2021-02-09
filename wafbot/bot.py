#main bot.py
import discord
from discord.utils import get
from discord import Member
from discord.ext import commands
from discord.voice_client import VoiceClient
import os
from os import path
import nacl
import asyncio
import records
import random
import youtube_dl
from gamesnstuff import *
from info import *
from ppl import *
from moderation import *
from music import *
from thing import *
import logging
import json
import praw 
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
import urllib.parse, urllib.request, re
import wavelink

intents = discord.Intents.default()


#define the bot
client = discord.Client(intents=intents)
bot = commands.Bot
#logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)



@client.event
async def on_message(msg):

    
    #basic commands and responses for fun
    
    if msg.content.startswith("pong"):
        await msg.channel.send("ping")
               
    if msg.content.lower() == "e":
        await msg.delete()
        await msg.channel.send("stfu")
        
    if msg.content.startswith ("stfu"):
        await msg.delete()
    
    if msg.content.startswith("bruh"):
        e = "🤔"
        await msg.add_reaction(e)

    if msg.content.startswith("bots suck"):
        await msg.channel.send("humans suck")
        
    if msg.author.id == 155149108183695360:
        if msg.guild.id == 762718463575064636:
            await msg.channel.send("Who brought this stupid bot back ban this fricking idiot right now")
        

    if "69" in msg.content:
        user = msg.author
        if user.bot == False:
            await msg.channel.send("*nice*")

        
    if msg.content.startswith("uno reverse card"):
        await msg.channel.send("no")
        
    if "bye" in msg.content.lower() or "goodnight" in msg.content.lower() or "cya" in msg.content.lower():
        user = msg.author
        if user.bot == False:
            await msg.channel.send("cya later! come back soon!")
        
   
        
    if msg.content.startswith("how are you waf bot"):
        r = "I'm doing great thanks for asking"
        r1 = "I'm drunk again!"
        r3 = "why do you care?"
        r4 = "I'm doing just fine."
        r5 = "im doin pretty good, how are you"
        res = [r,r1,r3,r4]
        async with msg.channel.typing():
                await asyncio.sleep(1)
        await msg.channel.send(random.choice(res))
    
    if msg.content.startswith("hello wa") or msg.content.startswith("hey wa") or msg.content.startswith("hi wa") or msg.content.startswith("yo wa") or msg.content.startswith("bonjour"):
        user = msg.author
        if user.bot == False:
            await msg.channel.send("ello there " + str(user.mention) + "!")

    if msg.content.startswith("love you waf bot"):
        e1 = ":heart:"
        e2 = "i hate you"
        e3 = "fak off"
        es = [e1, e2, e3]
        e = random.choice(es)
        await msg.channel.send(e)
        
    if "sleep" in msg.content.lower():
        user = msg.author
        if user.bot == False:
            await msg.channel.send("Hey you kid you need to go to sleep so get out of here and sleep before i kick you stop texting in discord servers its sleepy time so get the frick out of here")
        
    if msg.content.startswith("good job waf bot"):
        id = msg.author.id
        user = discord.Object(id)
        user.mention = id
        user.display_name = f"<@{id}>"
        await msg.channel.send("you too " + str(user.display_name))
        
    if "dyno" in msg.content.lower():
        user = msg.author
        if user.bot == False:
            if msg.guild.id == 762718463575064636:
                async with msg.channel.typing():
                    await asyncio.sleep(2)
                await msg.channel.send("dyno is the worst bot ever he sucks and should die in a hole frick dyno why would you even mention him hes so bad we hate dyno i will fight him frick you dyno")
            
    if msg.content.startswith("waf bot"):
        await msg.channel.send("thats me!")
   
    if client.user.mentioned_in(msg):
        if msg.author.bot == False:
            await msg.channel.send("thats me!")

    if msg.content.startswith("test"):
        await msg.add_reaction("👍")    

        
    if msg.content.startswith("tell me a joke") or msg.content.startswith("Tell me a joke"):
        async with msg.channel.typing():
                await asyncio.sleep(2)
        await joke(msg)

    if msg.author.id == 698707989531459595:
        numb = random.randint(1,3)
        if numb == 2:
            await msg.add_reaction("🧇")

    for user in msg.mentions:
        if msg.author.bot == False:
            role = discord.utils.get(msg.guild.roles , name='afk')
            if role in user.roles:
                await msg.channel.send("That user is AFK.")
    role = discord.utils.get(msg.guild.roles , name='afk')
    if role in msg.author.roles:
        await msg.author.remove_roles(role)
        await msg.channel.send("You are no longer AFK.")
    
    
      # attempted to optimize, not working rn
        # elif msg.content[0:5] == "=join":
        #     await join(client, msg)

        # elif "leave" in msg.content:
        #     await leave(client, msg)

        # elif "play" in msg.content:
        #     await play(client, msg)

        # else:
        #     try:
        #         exec("await " + msg.content[1:]+"(msg)")
        #     except Exception as e:
        #         print(str(e))
        #         embed=discord.Embed(title="Invalid Command.", description="Do =help for a list of commands.", color=0x06f459)
        #         embed.set_footer(text="Contact STUFFEDWAFFLES8367 for more information on bot")
        #         await msg.channel.send(embed=embed)  

       

    
    if msg.content.startswith("="):
        if "=ping" in msg.content:
            async with msg.channel.typing():
                await asyncio.sleep(2)
            message = await msg.channel.send(f'Pong!🏓')
            await asyncio.sleep(1)
            await message.edit(content=f'Pong!🏓\n`Responded in {round(client.latency * 1000)}ms`')
            


        if "=user" in msg.content:
            await users(msg)
            


        if "=waffle" in msg.content:
            await waffle(msg)
            


        if "=jedi" in msg.content:
            await jedi(msg)
            


        if "=para" in msg.content:
            await para(msg)
            

        if "=ched" in msg.content:
            await ched(msg)
            

        if "=rickroll" in msg.content:
            await rick(msg)
            

        if "=destiny" in msg.content:
            await destiny(msg)
            

        if "=daky" in msg.content:
            await daky(msg)
           

        if "=aqwuah" in msg.content:
            await aqwuah(msg)
           

            #info stuff
        
        
        if "=help fun" in msg.content:
            await helpfun(msg)
            
        
        if "=help mod" in msg.content:
            await helpmod(msg)
            
        
        if "=help info" in msg.content:
            await helpinfo(msg)
            
        
        if "=help music" in msg.content:
            await helpmusic(msg)
           
        
        if msg.content == "=help":
            await help(msg)
            

        if "=botinfo" in msg.content:
            await botinfo(msg)
            
        
        if "=serverinfo" in msg.content:
            await serverinfo(msg)
            

        if "=hypickle" in msg.content:
            await hypickle(msg)
            
        if "=invite" in msg.content:
            await invite(msg)
           

        if "=myid" in msg.content:
            await myid(msg)
                

        if "=github" in msg.content:
            await github(msg)
           
        

            #games
        if "=dog" in msg.content:
            await dog(msg)
           

        if "=cat" in msg.content:
            await cat(msg)
            

        if "=rps" in msg.content:
            await rps(msg)
            
        
        if "=roll" in msg.content:
            await roll(msg)
            
        
        if "=say" in msg.content:
            await say(msg)
            

        if "=afk" in msg.content:
            await afk(msg)
            
        
        if "=google" in msg.content:
            await google(msg)
            
        
        if "=poll" in msg.content:
            await poll(msg)
            
        
        if "=flip" in msg.content:
            await flip(msg)
           
        
        if "=meme" in msg.content:
            await meme(msg)
            
        
        if "=cursed" in msg.content:
            await cursed(msg)
            
        
        if "=nsfw" in msg.content:
            await nsfw(msg)
        
        if "=horror" in msg.content:
            await horror(msg)
            

        if "=kill" in msg.content:
            await kill(msg)
            

        if "=rr" in msg.content:
            await russianroulette(msg)
            
        
        if "=st" in msg.content:
            await thoughts(msg)
            

        if "=aww" in msg.content:
            await aww(msg)
            
        
        if "=wholesome" in msg.content:
            await wholesome(msg)
            

            #mod commands
        if "=kick" in msg.content:
            await kick(msg)
            

        if "=ban" in msg.content:
            await ban(msg)
            
        
        if "=blist" in msg.content:
            await banlist(msg)
            

        if "=mute" in msg.content:
            await mute(msg)
            

        if "=unmute" in msg.content:
            await unmute(msg)
            

        if "=nick" in msg.content:
            await nick(msg)
            

        if "=addrole" in msg.content:
            await addrole(msg)
            
        
        if "=warn" in msg.content:
            await warn(msg)
            

        if "=dm" in msg.content:
            await dm(msg)
            

        if "=delrole" in msg.content:
            await delrole(msg)
            
        
        if "=shutdown" in msg.content:
            await shutdown(client, msg)
            
        
        if "=yeet" in msg.content:
            await yeet(msg)
            
        
        if "=channeladd" in msg.content:
            await channeladd(msg)
            
        
        if "=roleadd" in msg.content:
            await roleadd(msg)
            

        # music
        if "=join" in msg.content:
            await join(client, msg)
            

        if "=leave" in msg.content:
            await leave(client, msg)
            

        if "=play" in msg.content:
            await play(client, msg)
            
        
        if "=pause" in msg.content:
            await pause(client, msg)
            
        
        if "=resume" in msg.content:
            await resume(client, msg)
            
        
        if "=video" in msg.content:
            await video(msg)
            

        if "=queue" in msg.content:
            await queue(msg)
            
        
        if "=clear" in msg.content:
            await clear(client, msg)
           

        if "=loop" in msg.content:
            await loop(client, msg)
            
        
        if "=remove" in msg.content:
            await remove(client, msg)
            
        

        if "=smite" in msg.content:
            await smite(msg)
            
        
        if "=command" in msg.content:
            await uselesscommand(msg)
            

        if "=announce" in msg.content:
            await announce(msg)
            
        
        if "=bigletters" in msg.content:
            await bigletters(msg)
            
        

       
    
        

        if msg.content.startswith("="):
            print(f'{msg.author} ran command {msg.content} at {msg.created_at.strftime("%a, %b %d %Y at %H:%M:%S %p")} in {msg.channel}')



#welcome and leave      
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name='Member')
    channel = client.get_channel(762718464124125226)
    await member.add_roles(role)
    
    await channel.send("Hey there " + member.mention + "! Welcome to " + str(member.guild.name) + "! If you need any help feel free to ask the admins, and to see a list of my commands do =help in #bot-commands. Enjoy your stay!")
       
#bot status + game
@client.event
async def on_ready():
    
    
    
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name="nothing. | type =help"))
    
    
    print(f'Bot connected as {client.user.name}')

 
   

with open(os.getcwd()+"/secrets.json") as f:
    secrets = json.load(f)

client.run(secrets['token'])
