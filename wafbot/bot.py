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
import logging
import json
import praw 
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
import urllib.parse, urllib.request, re
import wavelink
import requests
import aiohttp 
from gamesnstuff import *
from info import *
from ppl import *
from moderation import *
from music import *

intents = discord.Intents.default()
intents.members = True 


client = discord.Client(intents=intents, command_prefix="=")
bot = commands.Bot(command_prefix="=")
#logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)



@client.event
async def on_message(msg):
   
    #basic responses 
              
    if msg.content.lower() == "e":
        await msg.delete()
        respond = await msg.channel.send("stfu")
        await respond.delete()
    
    if msg.content.startswith("bruh"):
        await msg.add_reaction("🤔")
    
    if "69" in msg.content:
        if msg.author.bot == False:
            await msg.channel.send("***nice***", delete_after=5)
        
    if msg.content.startswith("uno reverse card"):
        await msg.channel.send("double uno reverse card")
        
    if "bye waf bot" in msg.content or "cya waf bot" in msg.content or "goodnight waf bot" in msg.content:
        if msg.author.bot == False:
            async with msg.channel.typing():
                await asyncio.sleep(1)
            await msg.channel.send(f"cya later {msg.author.mention}!")
        
   
        
    if "how are you waf bot" in msg.content or "how you doing waf bot" in msg.content or "whats up waf bot" in msg.content or "how r u waf bot" in msg.content or "hows life waf bot" in msg.content:
        if msg.author.bot == False:
            r = "I'm doing great, how are you"
            r1 = "I'm drunk again! how you doin buddy?"
            r3 = "im depressed, how are you"
            r4 = "I'm doing just fine. how are you?"
            r5 = "im doin pretty good, how are you"
            res = [r,r1,r3,r4, r5]
            async with msg.channel.typing():
                    await asyncio.sleep(1)
            await msg.channel.send(random.choice(res))

            def check(m):
                return m.channel == msg.channel and m.author == msg.author
            message = await client.wait_for("message", check=check)

            if "good" in msg.content or "happy" in msg.content or "great" in msg.content or "decent" in message.content:
                async with msg.channel.typing():
                    await asyncio.sleep(1)
                await msg.channel.send("Thats good to hear!")
            if "bad" in msg.content or "eh" in msg.content or "sad" in msg.content or "depress" in message.content:
                async with msg.channel.typing():
                    await asyncio.sleep(1)
                await msg.channel.send("I'm sorry to hear that, i hope things improve! if you need anything let the admins here know so they can help!")
    
    if "thank" in msg.content and "waf bot" in msg.content:
        await msg.channel.send(f"Np, {msg.author.mention}!") 
    
    if "hello waf bot" in msg.content or "hey waf bot" in msg.content or "hi waf bot" in msg.content or "yo waf bot" in msg.content or "bonjour" in msg.content:
        if msg.author.bot == False:
            async with msg.channel.typing():
                await asyncio.sleep(1)
            await msg.channel.send(f"hey there {msg.author.mention}!")

    if "love you waf bot" in msg.content.lower():
        e1 = ":heart:"
        e2 = "i hate you"
        e3 = "fak off"
        e4 = "leave me alone"
        e5 = ":middle_finger:"
        es = [e1, e2, e3, e4, e5]
        await msg.channel.send(random.choice(es))
        
    if "dyno" in msg.content.lower():
        if msg.author.bot == False:
            async with msg.channel.typing():
                await asyncio.sleep(2)
            await msg.channel.send("dyno is the worst bot ever he sucks and should die in a hole frick dyno why would you even mention him hes so bad we hate dyno i will fight him frick you dyno")
            
    if msg.content.lower() == "waf bot":
        await msg.channel.send("thats me!")
   
    if client.user.mentioned_in(msg):
        if msg.author.bot == False:
            await msg.channel.send(f"hey {msg.author.mention}, whatcha need?")
  
    if "tell me a joke" in msg.content.lower():
        async with msg.channel.typing():
                await asyncio.sleep(2)
        await joke(msg)        

    for user in msg.mentions:
        if msg.author.bot == False:
            role = discord.utils.get(msg.guild.roles , name='afk')
            if role in user.roles:
                await msg.channel.send("That user is AFK.")
    role = discord.utils.get(msg.guild.roles , name='afk')
    if role in msg.author.roles:
        await msg.author.remove_roles(role)
        await msg.channel.send("You are no longer AFK.")
    

    
    if msg.content.startswith("="):
        if "=ping" in msg.content:
            message = await msg.channel.send(f'Pong!🏓')
            async with msg.channel.typing():
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
        
        if "=timer" in msg.content:
            await timer(msg)
           
        if "=meme" in msg.content:
            await meme(msg)
            
        if "=cursed" in msg.content:
            await cursed(msg)
            
        if "=kill" in msg.content:
            await kill(msg)
            
        if "=rr" in msg.content:
            await russianroulette(msg)
            
        if "=showerthought" in msg.content:
            await thoughts(msg)
        
        if "=aww" in msg.content:
            await aww(msg)
            
        if "=wholesome" in msg.content:
            await wholesome(msg)
        
        if "=urban" in msg.content:
            await urban(msg)
            
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
        
        if "=channeldel" in msg.content:
            await channeldel(msg)
            
        if "=roleadd" in msg.content:
            await roleadd(msg)
        
        if "=roledel" in msg.content:
            await roledel(msg)

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
        
        if "=np" in msg.content:
            await np(msg)

        if "=yoink" in msg.content:
            await yoink(msg)
        
        if "=queue" in msg.content:
            await queue(msg)
            
        if "=clear" in msg.content:
            await clear(client, msg)
        
        if "=loop" in msg.content:
            await loop(client, msg)
            
        if "=remove" in msg.content:
            await remove(client, msg)
        
        if "=voicekick" in msg.content:
            await voicekick(client, msg)

        if "=smite" in msg.content:
            await smite(msg)
        
        if "=announce" in msg.content:
            await announce(msg)
        
        if "=bigletters" in msg.content:
            await bigletters(msg)
            
        

       
    
        

        if msg.content.startswith("="):
            print(f'{msg.author} ran command {msg.content} at {msg.created_at.strftime("%a, %b %d %Y at %H:%M:%S %p")} in {msg.channel}')



#welcome and leave      
@client.event
async def on_member_join(member):
    await member.send("Hey there " + member.mention + "! Welcome to **" + str(member.guild.name) + "**! If you need any help feel free to ask the admins, and to see a list of my commands do `=help` in the bot commands channel. Enjoy your stay!")

#bot status 
@client.event
async def on_ready():    
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name="minecraft alone | type =help"))
    print(f'Bot connected as {client.user.name}')
     
   

with open(os.getcwd()+"/secrets.json") as f:
    secrets = json.load(f)

client.run(secrets['token'])


