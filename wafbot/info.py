#copy bot info, server info, user, stuff like that here
import discord
from discord.utils import get
from discord import Member
from discord.ext import commands
import os
import youtube_dl
from discord.voice_client import VoiceClient
import random

client = discord.Client()

async def help(msg):
    embed=discord.Embed(title="Waf Bot Help!", description="Waf Bot is a simple bot made for the le Kingdom SMP server. To see everything Waf Bot can do, check the github!", color=0x06f459)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/762718464124125226/805548671198298122/Screenshot_2021-01-31_at_19.28.48.png")
    embed.add_field(name="Fun commands-", value="`=help fun`", inline=False)
    embed.add_field(name="Mod commands-", value="`=help mod`", inline=False)
    embed.add_field(name="Server/info commands-", value="`=help info`", inline=False)
    embed.add_field(name="Music commands-", value="`=help music`", inline=False)
    embed.set_footer(text="Contact STUFFEDWAFFLES8367 for more info on bot")
    await msg.channel.send(embed=embed)

async def helpfun(msg):
    embed=discord.Embed(title="Waf Bot fun commands!", description="For other commands, do =help.", color=0x06f459)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/762718464124125226/805548671198298122/Screenshot_2021-01-31_at_19.28.48.png")
    embed.add_field(name="Twitch/YT channels!", value="`=jedi` - info about Jedi \n`=ched` - info about ched \n`=destiny` - info about destiny \n`=daky` - info about dak \n`=aqwuah` - info about aqwuah", inline=False)
    embed.add_field(name="Other-", value="`=waffle` - waffles! \n`=para` - para! \n`=rickroll` - rickroll people \n`=dog` - get a doggo pic! \n`=cat` - get a catto pic! \n`=roll` - roll a die \n`=rps` - play rock, paper, scissors with the bot \n`=dm` - dm a user \n`ping` - get a response and client latency \n`=afk` - set an afk status to let others know you are afk", inline=False)
    embed.set_footer(text="Contact STUFFEDWAFFLES8367 for more info on bot")
    await msg.channel.send(embed=embed)

async def helpmod(msg):
    embed=discord.Embed(title="Waf Bot moderator commands!", description="For other commands, do =help.", color=0x06f459)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/762718464124125226/805548671198298122/Screenshot_2021-01-31_at_19.28.48.png")
    embed.add_field(name="Banning, Kicking, Muting-", value="`=ban` - ban a user \n`=blist` - get a list of banned users \n`=kick` - kick a user \n`=mute` - mute a user \n`=unmute` - unmute a user \n`=warn` - warn a user", inline=False)
    embed.add_field(name="Moderator only commands-", value="`=say` - make the bot say something \n`=nick` - give a user a nickname \n`=addrole` - add a role to a user \n`=delrole` - remove a role from a user \n`=shutdown` - shut the bot down if needed \n`=yeet` - clear a certain number of messages from a chat", inline=False)
    embed.set_footer(text="Contact STUFFEDWAFFLES8367 for more info on bot")
    await msg.channel.send(embed=embed)

async def helpinfo(msg):
    embed=discord.Embed(title="Waf Bot info commands!", description="For other commands, do =help.", color=0x06f459)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/762718464124125226/805548671198298122/Screenshot_2021-01-31_at_19.28.48.png")
    embed.add_field(name="Server info-", value="`=serverinfo` - get info about the server \n`=invite` - get an invite to a server that probably isn't yours \n`=hypickle` - hypixel info \n`=help` - the command you did to get here", inline=False)
    embed.add_field(name="User/bot info-", value="`=user` - get info about a user \n`=myid` - get your id \n`=botinfo` - get info about bot \n`=github` - get the bots github link for the code", inline=False)
    embed.set_footer(text="Contact STUFFEDWAFFLES8367 for more info on bot")
    await msg.channel.send(embed=embed)

async def helpmusic(msg):
    embed=discord.Embed(title="Waf Bot music commands!", description="For other commands, do =help.", color=0x06f459)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/762718464124125226/805548671198298122/Screenshot_2021-01-31_at_19.28.48.png")
    embed.add_field(name="All Music Commands-", value="`=join` - makes the bot join a vc and rickroll you for 10 seconds \n`=leave` - makes the bot leave vc \n`=play` - plays a song(currently doesnt work) \n`=pause` - pause the currently playing song \n`=resume` - resume the currently playing song \n`=url` - get a video link from a query \n`=queue` - get the list of songs in the queue \n`=clear` - clear the queue", inline=False)
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
        id = user.id
        avatar = user.avatar_url
        date = user.created_at
        usersnick = user.display_name
        if user.bot == True:
            bot = "Yes."
        elif user.bot == False:
            bot = "No."
        embed=discord.Embed(title="User- " + str(user), description="User ID- " + str(id), color=0x06f459)
        embed.set_author(name=str(user))
        embed.add_field(name="Account Created", value="Created- " + str(date), inline=False)
        embed.add_field(name="Bot? ", value=str(bot), inline=True)
        embed.add_field(name="Nick-", value=str(usersnick), inline=True)
        embed.set_image(url=str(avatar))
        embed.set_footer(text="Contact STUFFEDWAFFLES8367 for more information on bot")
        await msg.channel.send(embed=embed)
    if not msg.mentions:
        user = msg.author
        id = msg.author.id
        avatar = (user.avatar_url)
        date = user.created_at
        usersnick = user.display_name
        if user.bot == True:
            bot = "Yes."
        elif user.bot == False:
            bot = "No."
        embed=discord.Embed(title="User- " + str(user), description="User ID- " + str(id), color=0x06f459)
        embed.set_author(name=str(user))
        embed.add_field(name="Account Created", value="Created- " + str(date), inline=False)
        embed.add_field(name="Bot? ", value=str(bot), inline=True)
        embed.add_field(name="Nick-", value=str(usersnick), inline=True)
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
      description="Description- " + description,
      color=0x06f459
    )
  embed.set_image(url=icon)
  embed.add_field(name="Server ID", value=id, inline=False)
  embed.add_field(name="Owner and Region", value=owner + "\n" + region, inline=False)
  embed.add_field(name="Member Count", value=memberCount, inline=True)
  embed.add_field(name="Channels", value=channels, inline=True)
  embed.set_footer(text="Contact STUFFEDWAFFLES8367 for more information on bot")

  await msg.channel.send(embed=embed)
    
    

        
async def hypickle(msg):
    await msg.channel.send("Hypixel IP- mc.hypixel.net \nAwesome PVP and Minigame server!")



async def invite(msg):
    await msg.channel.send("Here is an invite to the server: https://discord.gg/aCY6qSA88h")
    

async def myid(msg):
    await msg.channel.send(msg.author.id)
    print (msg.author.id)

async def github(msg):
    await msg.channel.send("Here is Waf Bot's code- https://github.com/stuffedwaffles/wafbot")


