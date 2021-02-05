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
    l1 = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ffilmdaily.co%2Fwp-content%2Fuploads%2F2020%2F04%2Fcat-play-lede-1300x867.jpg&f=1&nofb=1"
    l2 = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpeopledotcom.files.wordpress.com%2F2018%2F02%2Ftwo-tone-cat.jpg"
    l3 = "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.hdwallpaper.nu%2Fwp-content%2Fuploads%2F2017%2F04%2Fcat-11.jpg&f=1&nofb=1"
    l4 = "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fi.huffpost.com%2Fgen%2F1486888%2Fimages%2Fo-GRUMPY-CAT-facebook.jpg"
    l5 = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.purrform.co.uk%2Fwp-content%2Fuploads%2F2016%2F09%2Fcat-tonges.jpg"
    l6 = "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fimages.hellogiggles.com%2Fuploads%2F2016%2F02%2F27012831%2Fflickr-cat.jpg"
    l7 = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fd.newsweek.com%2Fen%2Ffull%2F1541596%2Fcat-generic.jpg"
    l8 = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.sciencenews.org%2Fwp-content%2Fuploads%2F2020%2F08%2F080720_eg_cat-covid_feat.jpg"
    l9 = "https://vethelpdirect.com/wordpress/wp-content/uploads/2019/09/cat-3620161_1920.jpg"
    catlinks = [l1,l2,l3,l4,l5,l6,l7,l8,l9]
    cat = random.choice(catlinks)
    embed=discord.Embed(title="MEOW!", color=0x06f459)
    embed.set_image(url=cat)
    embed.set_footer(text="Contact STUFFEDWAFFLES8367 for more information on bot")
    await msg.channel.send(embed=embed)

@client.event
async def dog(msg):
    l1 = "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2F1.bp.blogspot.com%2F-1uQRYMklACU%2FToQ6aL-5uUI%2FAAAAAAAAAgQ%2F9_u0922cL14%2Fs1600%2Fcute-puppy-dog-wallpapers.jpg"
    l2 = "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2F3.bp.blogspot.com%2F-1fRaPu5_U9s%2FUWLerAZHutI%2FAAAAAAAAhbY%2FOQzHm7uEijg%2Fs1600%2Fcute-dog-pictures-016.jpg"
    l3 = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pixelstalk.net%2Fwp-content%2Fuploads%2F2016%2F08%2F2560x1600-Funny-Dog-Wallpaper-1.jpg"
    l4 = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2F2.bp.blogspot.com%2F-vB-YclIA1bM%2FUU9BOJ12MiI%2FAAAAAAAAg4A%2F2hKr5DeLF80%2Fs1600%2Fcute-puppy-pictures-025.jpg"
    l5 = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.rover.com%2Fblog%2Fwp-content%2Fuploads%2F2015%2F04%2Fboo-pomeranian.jpg"
    l6 = "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.dog-learn.com%2Fdog-breeds%2Fmaltese%2Fimages%2Fmaltese-u3.jpg"
    l7 = "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fbarkpost.com%2Fwp-content%2Fuploads%2F2014%2F07%2Fpuppy_dog_eyes_cute.jpg"
    l8 = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwhyy.org%2Fwp-content%2Fuploads%2F2018%2F12%2Fpet_show_stern_dog_2100.jpg"
    l9 = "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.pixelstalk.net%2Fwp-content%2Fuploads%2F2016%2F04%2FGolden-retriever-dogs-high-definition-wallpapers.jpg"
    l10 = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.ytimg.com%2Fvi%2FWOq7n3nDqWI%2Fmaxresdefault.jpg"
    l11 = "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fr.ddmcdn.com%2Fs_f%2Fo_1%2Fw_1024%2Fh_681%2FAPL%2Fuploads%2F2013%2F06%2FActiveDogBenefits.jpg&f=1&nofb=1"
    doglinks = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11]
    dog = random.choice(doglinks)
    embed=discord.Embed(title="WOOF!", color=0x06f459)
    embed.set_image(url=dog)
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
        flipp = "Heads!"

    if number == 2:
        flipp = "Tails!"

    await msg.channel.send(str(flipp))




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
        channel = client.get_channel(762718464124125226)
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
        