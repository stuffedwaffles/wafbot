#bot info, serverinfo, help, etc
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

client = discord.Client()

async def help(msg):
    embed=discord.Embed(title="Waf Bot Help!", description="Waf Bot is a simple bot made for the le Kingdom SMP server. To see everything Waf Bot can do, check the github!", color=0x06f459)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/762718464124125226/805548671198298122/Screenshot_2021-01-31_at_19.28.48.png")
    embed.add_field(name="Fun commands-", value="`=help fun`", inline=True)
    embed.add_field(name="Mod commands-", value="`=help mod`", inline=True)
    embed.add_field(name="Server/info commands-", value="`=help info`", inline=True)
    embed.add_field(name="Music commands-", value="`=help music`", inline=True)
    embed.set_footer(text="Contact STUFFEDWAFFLES8367 for more info on bot")
    await msg.channel.send(embed=embed)

async def helpfun(msg):
    embed=discord.Embed(title="Waf Bot fun commands!", description="For other commands, do =help.", color=0x06f459)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/762718464124125226/805548671198298122/Screenshot_2021-01-31_at_19.28.48.png")
    embed.add_field(name="Twitch/YT channels!", value="`=jedi` - info about Jedi \n`=ched` - info about ched \n`=destiny` - info about destiny \n`=daky` - info about dak \n`=aqwuah` - info about aqwuah", inline=False)
    embed.add_field(name="Other-", value="`=waffle` - waffles! \n`=para` - para! \n`=rickroll` - rickroll people \n`=dog` - get a doggo pic! \n`=cat` - get a catto pic! \n`=meme` - get a random meme from reddit \n`=wholesome` - get a random wholesome image or meme \n`=aww` - get an image of a cute animal from reddit! \n`=st` - get a random shower thought to think about \n`=roll [number]` - roll a die \n`=flip` - flip a coin! \n`=rps [choice]` - play rock, paper, scissors with the bot \n`=rr` - play some russian roulette\n`=kill [user]` - kill a user", inline=False)
    embed.set_footer(text="Contact STUFFEDWAFFLES8367 for more info on bot")
    await msg.channel.send(embed=embed)

async def helpmod(msg):
    embed=discord.Embed(title="Waf Bot moderator commands!", description="For other commands, do =help.", color=0x06f459)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/762718464124125226/805548671198298122/Screenshot_2021-01-31_at_19.28.48.png")
    embed.add_field(name="Banning, Kicking, Muting-", value="`=ban [user]` - ban a user \n`=blist` - get a list of banned users \n`=kick [user]` - kick a user \n`=mute [user]` - mute a user \n`=unmute [user]` - unmute a user \n`=warn [user]` - warn a user", inline=False)
    embed.add_field(name="Moderator only commands-", value="`=say [message]` - make the bot say something \n`=dm [user] [message]` - dm a user \n`=nick [user] [nick]` - give a user a nickname \n`=addrole [role]` - add a role to a user \n`=delrole [role]` - remove a role from a user \n`=voicekick [user]` - kick a user from a voice channel\n`=shutdown` - shut the bot down if needed \n`=yeet [number or user]` - clear messages from a user or a certain number of messages \n`=channeladd [name] [voice/text]` - add a channel with a specified name and type \n`=channeldel [name]` - remove a specified channel \n`=roleadd [name]` - create a role with a specified name \n`=roledel [name]` - delete a role from the server", inline=False)
    embed.set_footer(text="Contact STUFFEDWAFFLES8367 for more info on bot")
    await msg.channel.send(embed=embed)

async def helpinfo(msg):
    embed=discord.Embed(title="Waf Bot info commands!", description="For other commands, do =help.", color=0x06f459)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/762718464124125226/805548671198298122/Screenshot_2021-01-31_at_19.28.48.png")
    embed.add_field(name="Server info-", value="`=serverinfo` - get info about the server \n`=invite` - get an invite to a server that probably isn't yours \n`=hypickle` - hypixel info \n`=help` - the command you did to get here \n`=help fun` - a list of fun commands \n`=help mod` - a list of moderator commands \n`=help info` - info and utility commands \n`=help music` - music and voice commands", inline=False)
    embed.add_field(name="User/bot info-", value="`=user [user]` - get info about a user \n`=myid` - get your id \n`=botinfo` - get info about bot \n`=github` - get the bots github link for the code", inline=False)
    embed.add_field(name="Utility Commands-", value="`=urban [query]` - get an urban dictionary definition of a word\n`=google [query]` - get a google result for a query \n`=poll [poll]` - start a poll(only use in the poll channel\n`ping` - get a response and client latency \n`=afk [reason]` - set an afk status to let others know you are afk", inline=False)
    embed.set_footer(text="Contact STUFFEDWAFFLES8367 for more info on bot")
    await msg.channel.send(embed=embed)

async def helpmusic(msg):
    embed=discord.Embed(title="Waf Bot music commands!", description="For other commands, do =help.", color=0x06f459)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/762718464124125226/805548671198298122/Screenshot_2021-01-31_at_19.28.48.png")
    embed.add_field(name="All Music Commands-", value="`=join` - makes the bot join a vc \n`=leave` - makes the bot leave vc \n`=play [song name or link]` - plays a song \n`=pause` - pause the currently playing song \n`=resume` - resume the currently playing song \n`=video [query]` - get a video link from a query \n`=queue` - get the list of songs in the queue \n`=clear` - clear the queue \n`=remove [number]` - remove a song from the queue", inline=False)
    embed.set_footer(text="Contact STUFFEDWAFFLES8367 for more info on bot")
    await msg.channel.send(embed=embed)


async def botinfo(msg):
    id = 783061816624021516
    date = "Nov 3rd, 2020"
    embed=discord.Embed(title="Waf Bot Info!", description="Do =help for a list of commands.", color=0x06f459)
    embed.add_field(name="Bot Command Prefix- ", value="=", inline=False)
    embed.add_field(name="Bot signed in as- ", value=str(f"<@{id}>"), inline=True)
    embed.add_field(name="Bot ID- ", value=str(id), inline=True)
    embed.add_field(name="Created by- ", value=str(f"<@{698707989531459595}>"), inline=False)
    embed.add_field(name="Created on- ", value=str(date), inline=True)
    embed.add_field(name="Other info-", value="Waf Bot is coded in discord.py by STUFFEDWAFFLES. It can be added to multiple servers, however, it was mainly made for Le Kingdom.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/762718464124125226/805548671198298122/Screenshot_2021-01-31_at_19.28.48.png")
    embed.set_footer(text="Contact STUFFEDWAFFLES8367 for more information on bot")

    await msg.channel.send(embed=embed)

async def users(msg):
    for user in msg.mentions:
        user = user
    if not msg.mentions:
        user = msg.author
    id = user.id
    avatar = user.avatar_url
    date = user.created_at.strftime("%a, %b %d %Y at %H:%M:%S %p")
    usersnick = user.display_name
    for role in user.roles:
        roles = role.name
    if user.bot == True:
        bot = "Yes."
    elif user.bot == False:
        bot = "No."
    embed=discord.Embed(title=f"User ID- {id}", color=0x06f459)
    embed.set_author(name=str(user))
    embed.add_field(name="Account Created", value=f"Created- {date}", inline=False)
    embed.add_field(name="Bot? ", value=str(bot), inline=True)
    embed.add_field(name="Nick-", value=str(usersnick), inline=True)
    embed.add_field(name="Highest Role-", value=str(roles), inline=False)
    embed.set_image(url=str(avatar))
    embed.set_footer(text="Contact STUFFEDWAFFLES8367 for more information on bot")
    await msg.channel.send(embed=embed)
    

async def serverinfo(msg):
  name = str(msg.guild.name)
  description = str(msg.guild.description)
  owner = str(msg.guild.owner)
  id = str(msg.guild.id)
  region = str(msg.guild.region)
  memberCount = str(msg.guild.member_count)
  icon = str(msg.guild.icon_url)
  channels = len(msg.guild.channels)

  embed = discord.Embed(
      title=name + " Server Info",
      description=f"Server Description- {description}",
      color=0x06f459
    )
  embed.set_image(url=icon)
  embed.add_field(name="Server ID", value=id, inline=False)
  embed.add_field(name="Owner and Region", value=f"{owner} \n{region}", inline=False)
  embed.add_field(name="Member Count", value=memberCount, inline=True)
  embed.add_field(name="Channels", value=channels, inline=True)
  embed.set_footer(text="Contact STUFFEDWAFFLES8367 for more information on bot")
  await msg.channel.send(embed=embed)
        
async def hypickle(msg):
    await msg.channel.send("Hypixel IP- mc.hypixel.net \nAwesome PVP and Minigame server! Has games such as Bedwars, Skywars, Murder Mystery, Mega Walls, Skyblock, and more!")

async def invite(msg):
    await msg.channel.send("Here is an invite to a server that you shouldn't join: https://discord.gg/aCY6qSA88h")

async def myid(msg):
    await msg.channel.send(msg.author.id)
    
async def github(msg):
    await msg.channel.send("Here is Waf Bot's code- https://github.com/stuffedwaffles/wafbot/tree/master")

async def timer(msg):
    time = int(msg.content.split(" ")[1])
    thing = str(msg.content.split(" ")[2])
    if "m" in thing:
        actualtime = float(time) * float(60)
        thingy = "minutes"
    if "s" in thing:
        actualtime = time
        thingy = "seconds"
    if "y" in thing:
        actualtime = float(time) * float(31536000)
        thingy = "years"
    if "d" in thing:
        actualtime = float(time) * float(86400)
        thingy = "days"
    if "h" in thing:
        actualtime = float(time) * float(3600)
        thingy = "hours"
    await msg.channel.send(f"Setting timer for {time} {thingy}.")
    await asyncio.sleep(actualtime)
    await msg.channel.send(f"{msg.author.mention}, your timer of {time} {thingy} is done!")


    