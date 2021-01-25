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
    embed=discord.Embed(title="Waf Bot Help!", description="Waf Bot is a simple bot made for the le Kingdom SMP server.", color=0x06f459)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/762718464124125226/800783415137534012/Screenshot_2021-01-18_at_17.46.37.png")
    embed.add_field(name="General Commands-", value="=ping, =dog, =cat, =waffle, =jedi, =ched, =para, =aqwuah, =destiny, =daky, =rps, =vantage, =hypickle, =rick, =roll. \n Also try asking for a joke!", inline=False)
    embed.add_field(name="Server and Mod commands-", value="=help, =botinfo, =serverinfo, =user, =addrole, =delrole, =ip, =kick, =ban, =mute, =unm, =invite, =nick, =warn, =dm, =shutdown, =myid, =say", inline=False)
    embed.add_field(name="Other-", value="Waf bot is coded in Python, for the code contact STUFFEDWAFFLES. The bot has a good amount of general fun commands, some basic moderator commands, and hopefully music queue and play commands soon! It can be added to multiple servers as well.")
    embed.set_footer(text="Contact STUFFEDWAFFLES8367 for more info on bot")

    await msg.channel.send(embed=embed)

async def botinfo(msg):
    id = 783061816624021516
    user = discord.Object(id)
    date = "Nov 3rd, 2020"
    embed=discord.Embed(title="Waf Bot Info!", description="Do =help for a list of commands and more details on bot", color=0x06f459)
    embed.add_field(name="Bot Command Prefix- ", value="=", inline=False)
    embed.add_field(name="Bot signed in as- ", value=str(f"<@{id}>"), inline=True)
    embed.add_field(name="Bot ID- ", value=str(id), inline=True)
    embed.add_field(name="Created by- ", value=str(f"<@{698707989531459595}>"), inline=False)
    embed.add_field(name="Created on- ", value=str(date), inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/762718464124125226/800783415137534012/Screenshot_2021-01-18_at_17.46.37.png")
    embed.set_footer(text="Contact STUFFEDWAFFLES8367 for more information on bot")

    await msg.channel.send(embed=embed)

async def user(msg):
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
    
    
async def ip(msg):
    await msg.channel.send("Server IP- LeKingdomSMP.aternos.me")
        
async def hypickle(msg):
    await msg.channel.send("Hypixel IP- mc.hypixel.net \nAwesome PVP and Minigame server!")

async def vantage(msg):
    await msg.channel.send("MCVantage 1.16 server! IP- play.mcvantage.us, Discord-https://discord.gg/y4e26tfuZH \n`waf bot does not reccommend joining vantage or their discord as they suck and the only person ever on the server is david so yeah this is useless why would you even run this command what is wrong with you`")

async def invite(msg):
    await msg.channel.send("Here is an invite to the server: https://discord.gg/aCY6qSA88h")
    

async def myid(msg):
    await msg.channel.send(msg.author.id)
    print (msg.author.id)



