import discord
from discord.utils import get
from discord import Member
from discord.ext import commands
from discord.voice_client import VoiceClient
import os
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
intents = discord.Intents.default()
intents.members = True

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

    guild = client.get_guild(762718463575064636)
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
        
   
        
    if msg.content.startswith("how are you waf bot?"):
        r = "I'm doing great thanks for asking"
        r1 = "I'm high!"
        r3 = "why do you care?"
        r4 = "I'm doing just fine."
        res = [r,r1,r3,r4]
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
        
    if msg.content.startswith("sleep"):
        id = msg.author.id
        user = discord.Object(id)
        user.mention = id
        user.display_name = f"<@{id}>"
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
            await msg.channel.send("dyno is the worst bot ever he sucks and should die in a hole frick dyno why would you even mention him hes so bad we hate dyno i will fight him frick you dyno")
    
    if msg.content.startswith("waf bot"):
        await msg.channel.send("thats me!")
   
    if client.user.mentioned_in(msg):
        await msg.channel.send("thats me!")

    if msg.content.startswith("test"):
        await msg.add_reaction("👍")

    

        
    if msg.content.startswith("tell me a joke") or msg.content.startswith("Tell me a joke"):
        await joke(msg)

    if msg.author.id == 698707989531459595:
        numb = random.randint(1,3)
        if numb == 2:
            await msg.add_reaction("🧇")
            

    if msg.author.id == 737705917394583555:
        numb = random.randint(1,3)
        if numb == 2:
            await msg.add_reaction("✈️")
    
    
        

       

    if msg.content.startswith("="):
        #people cmds
        if "waffle" in msg.content:
            await waffle(msg)

        elif "jedi" in msg.content:
            await jedi(msg)

        elif "para" in msg.content:
            await para(msg)

        elif "ched" in msg.content:
            await ched(msg)

        elif "rick" in msg.content:
            await rick(msg)

        elif "destiny" in msg.content:
            await destiny(msg)

        elif "daky" in msg.content:
            await daky(msg)

        elif "aqwuah" in msg.content:
            await aqwuah(msg)

        elif "ping" in msg.content:
            await msg.channel.send(f'Pong!🏓\n`Responded in {round(client.latency * 1000)}ms`')
            #info stuff
        elif "help" in msg.content:
            await help(msg)
    
        elif "botinfo" in msg.content:
            await botinfo(msg)

        elif "user" in msg.content:
            await use(msg)
        
        elif "serverinfo" in msg.content:
            await serverinfo(msg)
        
        elif "ip" in msg.content:
            await ip(msg)

        elif "hypickle" in msg.content:
            await hypickle(msg)
        
        elif "vantage" in msg.content:
            await vantage(msg)

        elif "invite" in msg.content:
            await invite(msg)

        elif "myid" in msg.content:
            await myid(msg)        

            #games
        elif "dog" in msg.content:
            await dog(msg)

        elif "cat" in msg.content:
            await cat(msg)

        elif "rps" in msg.content:
            await rps(msg)
        
        elif "roll" in msg.content:
            await roll(msg)
        
        elif "say" in msg.content:
            await say(msg)

            #mod commands
        elif "kick" in msg.content:
            await kick(msg)

        elif "ban" in msg.content:
            await ban(msg)

        elif "mute" in msg.content:
            await mute(msg)

        elif "unm" in msg.content:
            await unmute(msg)

        elif "nick" in msg.content:
            await nick(msg)

        elif "addrole" in msg.content:
            await addrole(msg)
        
        elif "warn" in msg.content:
            await warn(msg)

        elif "dm" in msg.content:
            await dm(msg)

        elif "delrole" in msg.content:
            await delrole(msg)
        
        elif "shutdown" in msg.content:
            await shutdown(client, msg)

    
        
        #music
        elif "join" in msg.content:
            await join(client, msg)

        elif "leave" in msg.content:
            await leave(client, msg)

        elif "play" in msg.content:
            await play(client, msg)
        
        
        else:
            embed=discord.Embed(title="Invalid Command.", description="Do =help for a list of commands.", color=0x06f459)
            embed.set_footer(text="Contact STUFFEDWAFFLES8367 for more information on bot")
            await msg.channel.send(embed=embed)
    #logging commands n stuff ish
        guild = client.get_guild(762718463575064636)
        channel = client.get_channel(801262872955977729)
        embed=discord.Embed(title=str(msg.author), description=None, color=0x06f459)
        embed.add_field(name="ran a command in " + str(msg.channel), value="`" + str(msg.content) + "` at " + str(msg.created_at.strftime("%a, %b %d %Y at %H:%M:%S %p")))
        embed.set_footer(text="Contact STUFFEDWAFFLES8367 for more info on bot")
        await channel.send(embed=embed)
        print (msg.author + " ran command " + msg.content + " at " + str(msg.created_at.strftime("%a, %b %d %Y at %H:%M:%S %p")))





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
    guild = client.get_guild(762718463575064636)
    channel = client.get_channel(801262872955977729)
    
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="netflix! | type =help"))
    await channel.send("Bot is online!", delete_after=2.0)
    
    print("ayo ready to kode")
    
    

import json

with open("secrets.json") as f:
    secrets = json.load(f)

client.run(secrets['token'])
