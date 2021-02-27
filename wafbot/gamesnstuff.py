#games/memes
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
import logging
import json
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
import urllib.parse, urllib.request, re
import wavelink
import requests

client = discord.Client()

@client.event
#rps, joke, cat, dog
async def rps(msg):
    r = "rock"
    s = "scissors"
    p = "paper"
    rand = ""
    #string
    rps = [r,p,s]
    user_choice = msg.content.split(" ")[1] #=rps user_choice
    # index 0 = item 1, index 1 = item 2, ...
    # list[1] = second item of list
    #msg.content.split(" ")[1] gets the second item from the user message
    rand = random.choice(rps)
    # DEBUGGING: SENDING THE VARIABLES SO THAT WE CAN FIGURE OUT WHAT'S GOIN ON
    await msg.channel.send("Computer Choice (randomly generated): ||" + str(rand) + "|| \nUser Choice: " + str(user_choice))
            
    if (rand == r and user_choice == "rock"):
            await msg.channel.send("Its a tie!")
    elif (rand == s and user_choice == "rock"):
            await msg.channel.send("you crushed my scissors. you win!")
    elif (rand == p and user_choice == "rock"):
            await msg.channel.send("My paper covered your rock. you lost!")
    elif (rand == r and user_choice =="paper"):
        await msg.channel.send("You covered the rock. you win!")
    elif (rand == s and user_choice =="paper"):
        await msg.channel.send("I cut your paper! i win!")
    elif (rand == p and user_choice =="paper"):
        await msg.channel.send("Its a tie!")        
    elif (rand == r and user_choice =="scissors"):
        await msg.channel.send("I crushed your scissors. you lost!")
    elif (rand == p and user_choice =="scissors"):
        await msg.channel.send("You cut my paper. you win!")
    elif (rand == s and user_choice =="scissors"):
        await msg.channel.send("Its a tie!")       

@client.event
async def joke(msg):
    j1 = "Why are fish so smart? \n ||Because they live in schools!||"
    j2 = "Where do polar bears keep their money? \n ||In a snow bank!||"
    j3 = "Why did the pony get sent to his room? \n ||Because he wouldn't stop horsing around.||"
    j4 = "What did the fisherman say to the magician? \n ||Pick a cod, any cod!||"
    j5 = "Why is Cinderella bad at soccer? \n ||Because she is always running away from the ball.||"
    j6 = "Why do bicycles fall over? \n ||Because they are two-tired.||"
    j7 = "Why did the cookie go to the nurse? \n ||Because he felt crummy.||"
    j8 = "What kind of room doesn't have doors? \n ||A mushroom!||"
    j9 = "Whats the best part of a waffle? \n ||The w. Without it it's just awful.||"
    j10 = "What do you call a waffle dropped on the beach? \n ||Sandy eggo.||"
    jokelist = [j1,j2,j3,j4,j5,j6,j7,j8,j9,j10]
    await msg.channel.send(random.choice(jokelist))

@client.event
async def cat(msg):
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/catpictures/new.json?sort=hot') as r:
            res = await r.json()
    embed=discord.Embed(title="MEOW!", color=0x06f459)
    embed.set_image(url=(res['data']['children'] [random.randint(0, 25)]['data']['url']))
    embed.set_footer(text="Contact STUFFEDWAFFLES8367 for more information on bot")
    await msg.channel.send(embed=embed)

@client.event
async def dog(msg):
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dogpictures/new.json?sort=hot') as r:
            res = await r.json()
    embed=discord.Embed(title="WOOF!", color=0x06f459)
    embed.set_image(url=(res['data']['children'] [random.randint(0, 25)]['data']['url']))
    embed.set_footer(text="Contact STUFFEDWAFFLES8367 for more information on bot")
    await msg.channel.send(embed=embed)  

@client.event
async def aww(msg):
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/aww/new.json?sort=hot') as r:
            res = await r.json()
    embed=discord.Embed(title="AWWW!", color=0x06f459)
    embed.set_image(url=(res['data']['children'] [random.randint(0, 25)]['data']['url']))
    embed.set_footer(text="Contact STUFFEDWAFFLES8367 for more information on bot")
    await msg.channel.send(embed=embed)  

@client.event
async def horror(msg):
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/horrormemes/new.json?sort=hot') as r:
            res = await r.json()
    embed=discord.Embed(title="Enjoy some horror memes from reddit", color=0x06f459)
    embed.set_image(url=(res['data']['children'] [random.randint(0, 25)]['data']['url']))
    embed.set_footer(text="Contact STUFFEDWAFFLES8367 for more information on bot")
    await msg.channel.send(embed=embed) 

@client.event
async def thoughts(msg):
     async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/Showerthoughts/new.json?sort=hot') as r:
            res = await r.json()
        embed=discord.Embed(title="Heres a thought", description=(res['data']['children'] [random.randint(0, 25)]['data']['url']), color=0x06f459)
        embed.set_image(url=(res['data']['children'] [random.randint(0, 25)]['data']['url']))
        embed.set_footer(text="Contact STUFFEDWAFFLES8367 for more information on bot")
        await msg.channel.send(embed=embed)

@client.event
async def wholesome(msg):
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/wholesome/new.json?sort=hot') as r:
            res = await r.json()
    embed=discord.Embed(title="WHOLESOME IMAGES :D", color=0x06f459)
    embed.set_image(url=(res['data']['children'] [random.randint(0, 25)]['data']['url']))
    embed.set_footer(text="Contact STUFFEDWAFFLES8367 for more information on bot")
    await msg.channel.send(embed=embed) 

@client.event
async def roll(msg):
    numb2 = msg.content.split(" ")[1]
    roll = random.randint(1,int(numb2))
    await msg.channel.send("Bot rolled a dice! \nResult: " + str(roll))

@client.event
async def dm(msg):
    dmdm = msg.content.split(" ")[2:]
    dms = ''.join(dmdm)
    for user in msg.mentions:
        await user.send(str(dms))
        await msg.channel.send(user.mention + "has been dmed.")

@client.event
async def say(msg):
    words = msg.content
    wordss = words.replace("=say", "")
    await msg.delete()
    async with msg.channel.typing():
        await asyncio.sleep(2)
    await msg.channel.send(str(wordss))

@client.event
async def afk(msg):
    member = msg.author
    role = discord.utils.get(msg.guild.roles , name='afk')
    reasonn = msg.content
    reason = reasonn.replace("=afk ", "")
    if role not in member.roles:
        await member.add_roles(role)
        await msg.channel.send(member.mention + ", you are now AFK- " + reason)

@client.event
async def urban(msg):
    words = msg.content
    term = words.replace("=urban ", "")
    index = 1
    async with aiohttp.ClientSession() as session:  # Opens client session
            async with session.get("https://api.urbandictionary.com/v0/define", params={"term": term}) as r:  # Result
                result = await r.json()  # Parses file as json

            data = result["list"][index]  # Assigns list in dict as 'data'

            defin = data["definition"]  # Gets key value
            if "2." in defin:  # If there is a second definition
                defin = data["definition"].split("2.")  # Splits data
                defin = defin[0]  # Sets defin as first definition
            elif len(defin) > 250:  # Sets a 250 character limit
                defin = defin[:250]

            example = data["example"]  # Gets key value
            if "2." in defin:  # If there is a second example splits data
                example = data["example"].split("2.")  # Splits data
                example = example[0]  # Sets defin as first example
            elif len(example) > 250:   # Sets a 250 character limit
                example = example[:250]

            urban_embed = discord.Embed(title="Result- {0}".format(term),
                                        url=data["permalink"],
                                        color=0x06f459)
            # Creates# embed with a title with a hyperlink and set's the colour of the bar
            urban_embed.add_field(name="Definition", value=defin, inline=False)  # Adds field
            urban_embed.add_field(name="Example", value=example or "N/A", inline=False)
            urban_embed.add_field(name="👍", value=data["thumbs_up"], inline=True)
            urban_embed.add_field(name="👎", value=data["thumbs_down"], inline=True)
            urban_embed.set_footer(text="Author: " + data["author"])
            await msg.channel.send(embed=urban_embed)


@client.event
async def google(msg):

    quer =  msg.content
    query = quer.replace("=google ", "")

    try: 
        from googlesearch import search 
    except ImportError:  
        await msg.channel.send("No module named 'google' found") 


    for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
        await msg.channel.send(j) 

@client.event
async def poll(msg):

    pol = msg.content
    poll = pol.replace("=poll ", "")
    
    
    
    await msg.delete()
    
    react = await msg.channel.send("@everyone" + poll)
    await react.add_reaction("🇾")
    await react.add_reaction("🇳")

@client.event
async def flip(msg):
    number = random.randint(1,2)
    if number == 1:
        flipp = "🪙Heads!🪙"

    if number == 2:
        flipp = "🪙Tails!🪙"

    await msg.channel.send(str(flipp))

@client.event
async def meme(msg):
    embed=discord.Embed(title="Heres a meme!", color=0x06f459)
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            embed.set_footer(text="Contact STUFFEDWAFFLES for more info on bot")
            await msg.channel.send(embed=embed)

@client.event
async def cursed(msg):
    embed=discord.Embed(title="Cursed images!", color=0x06f459)
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/blursedimages/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            embed.set_footer(text="Contact STUFFEDWAFFLES for more info on bot")
            await msg.channel.send(embed=embed)

async def russianroulette(msg):
    number = random.randint(1,6)
    if number == 6:
        await msg.channel.send(str(msg.author.mention) + " was shot! Better luck next time! Oh wait, there wont be a next time-")
    else:
        await msg.channel.send("Good job " + str(msg.author.mention) + ", you survived!")

@client.event
async def kill(msg):
    for user in msg.mentions:
        c = str(user.mention) + " was told to do a backflip off a building by " + str(msg.author.mention)
        c1 = str(user.mention) + " was choked too hard by " + str(msg.author.mention)
        c2 = str(user.mention) + " annoyed " + str(msg.author.mention) + " and was stabbed to death."
        c3 = str(user.mention) + " was shot by " + str(msg.author.mention) + " with a frozen chicken."
        c4 = str(msg.author.mention) + " directed a wrecking ball towards " + str(user.mention) + "'s house."
        c5 = str(msg.author.mention) + " shoved " + str(user.mention) + " from their ego level to their IQ level."
        c6 = str(msg.author.mention) + " threw " + str(user.mention) + " into a snake pit."
        c7 = str(user.mention) + " was smashed too hard by " + str(msg.author.mention)
        c8 = str(user.mention) + " got thrown into a volcano by " + str(msg.author.mention) 
        c9 = str(msg.author.mention) + " threw an exploding kitten at " + str(user.mention)
        c10 = str(user.mention) + " attempted to attack " + str(msg.author.mention) + " and failed."
        c11 = str(msg.author.mention) + " buffed " + str(user.mention) + "'s banana too hard."
        clist = [c, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11]
        await msg.channel.send(random.choice(clist))

@client.event
async def smite(msg):
    if msg.author.id == 698707989531459595:
        if msg.mentions:
            for user in msg.mentions:
                await msg.channel.send(user.mention + " has been smited by waffles!")

async def uselesscommand(msg):
    if msg.author.id == 698707989531459595:
        await msg.channel.send("That command did nothing!")

async def announce(msg):
    if msg.author.id == 698707989531459595:
        
        announcee = msg.content
        announcement = announcee.replace("=announce", "")
        await msg.channel.send(announcement + "\n@everyone")
        await msg.delete()

async def bigletters(msg):
    if msg.author.id == 698707989531459595:
        letter = msg.content
        letters = letter.replace("=bigletters ", "")
        dictt = {'a':':regional_indicator_a:','b':':regional_indicator_b:','c':':regional_indicator_c:','d':':regional_indicator_d:','e':':regional_indicator_e:','f':':regional_indicator_f:','g':':regional_indicator_g:','h':':regional_indicator_h:',
        'i':':regional_indicator_i:','j':':regional_indicator_j:','k':':regional_indicator_k:','l':':regional_indicator_l:','m':':regional_indicator_m:','n':':regional_indicator_n:','o':':regional_indicator_o:','p':':regional_indicator_p:','q':':regional_indicator_q:',
        'r':':regional_indicator_r:','s':':regional_indicator_s:','t':':regional_indicator_t:','u':':regional_indicator_u:','v':':regional_indicator_v:','w':':regional_indicator_w:','x':':regional_indicator_x:','y':':regional_indicator_y:','z':':regional_indicator_z:', ' ':' '
        }
        arr = []
        for i in list(letters):
            for k, j in dictt.items():
                if k == i:
                    arr.append(j)
        await msg.channel.send(' '.join(arr))
        await msg.delete()


        