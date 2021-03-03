#moderation commands
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

client = discord.Client()
#mod commands

@client.event
async def kick(msg):
    
    member = msg.author
    if discord.utils.get(member.roles, name="Head Admin") is None:
        await msg.channel.send("You don't have permission to kick")
    else:
        for user in msg.mentions:
            await user.kick()
            await msg.channel.send(f"{user} has been kicked by {msg.author.mention}")
        
@client.event
async def ban(msg):
    member = msg.author
    if discord.utils.get(member.roles, name="Head Admin") is None:
        for user in msg.mentions:
            
            await msg.channel.send("You dont have permission to ban")
    else:
        for user in msg.mentions:
            
            await user.ban()
            await msg.channel.send(f"{user} has been banned by {msg.author.mention}")
        
async def banlist(msg):
    guild = msg.guild
    bans = await guild.bans()
    for ban in bans:
        await msg.channel.send(f"User name - `{ban.user.name}`, User ID - `{ban.user.id}`")

@client.event
async def mute(msg):
    
    member = msg.author
    if discord.utils.get(member.roles, name="Head Admin") is None:
        for user in msg.mentions:
            
            await msg.channel.send("You dont have permission to mute")
        
    else:
        for user in msg.mentions:
            voice = get(client.voice_clients, guild=msg.guild)
            role = discord.utils.get(msg.guild.roles, name='Muted')
            if role is None:
                role = await msg.guild.create_role(name='Muted')
            await user.add_roles(role)
            if voice == True:
                await user.edit(mute=True, deafen=True)
            await msg.channel.send(f"{user} has been muted by {msg.author.mention}")

async def unmute(msg):
    
    member = msg.author
    if discord.utils.get(member.roles, name="Head Admin") is None:
        for user in msg.mentions:
            
            await msg.channel.send("You dont have permission to unmute")
    else:
        for user in msg.mentions:
            
            role = discord.utils.get(msg.guild.roles, name='Muted')
            await user.remove_roles(role)
            await user.edit(mute=False, deafen=False)
            await msg.channel.send(f"{user} has been unmuted by {msg.author.mention}")

async def voicekick(client, msg):
    for user in msg.mentions:
        await user.edit(voice_channel=None)
        await msg.channel.send(f"{user.mention} has been kicked from voice.")

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
            await msg.channel.send(f"{user.mention}'s nick has been changed.")

async def warn(msg):
    warnin = msg.content.split(" ")[2:]
    warning = ''.join(warnin)
    for user in msg.mentions:
        await user.send(f"You have been warned on {user.guild.name} for {warning}")
        await msg.channel.send(f"{user.mention} has been warned.")
        

async def shutdown(client, msg):
    async with msg.channel.typing():
            await asyncio.sleep(1)
    await msg.channel.send("Shutting down...")
    await msg.delete()
    await client.logout()
    print ("Bot shutdown")

async def yeet(msg):
    if discord.utils.get(msg.author.roles, name="Head Admin") is None:
        await msg.channel.send("You can't do that.")
    else:
        await msg.delete()
        if msg.mentions:
            for user in msg.mentions:
                me = []
                async for m in msg.channel.history():
        
                    if m.author == user:
                        me.append(m)
                        await msg.channel.delete_messages(me)
                        await msg.channel.send(f"All messages by {user.mention} have been deleted.")
        else:
            llimit = msg.content.split(" ")[1]
            await msg.channel.purge(limit=int(llimit))
            await msg.channel.send(f"Chat cleared by {msg.author.mention}", delete_after=2.0) 

async def channeladd(msg):
    if discord.utils.get(msg.author.roles, name="Head Admin") is None:
        await msg.channel.send("You can't do that.")
    else:        
        channelname = msg.content.split(" ")[1]
        channeltype = msg.content.split(" ")[2]
        if str(channeltype) == "voice":
            channel = await msg.guild.create_voice_channel(str(channelname))
            await msg.channel.send(f"Voice Channel- `{channel}` has been created.")
        if str(channeltype) == "text":
            channel = await msg.guild.create_text_channel(str(channelname))
            await msg.channel.send(f"Text Channel- `{channel}` has been created.")

async def channeldel(msg):
    if discord.utils.get(msg.author.roles, name="Head Admin") is None:
        await msg.channel.send("You can't do that.")
    else:
        channel_name = msg.content.split(" ")[1]
        channel = discord.utils.get(msg.guild.channels, name=channel_name)
        await channel.delete()
        await msg.channel.send("Channel has been deleted.")

async def roleadd(msg):
    if discord.utils.get(msg.author.roles, name="Head Admin") is None:
        await msg.channel.send("You can't do that.")
    else:
        rolename = msg.content.split(" ")[1]
        await msg.guild.create_role(name=str(rolename))
        await msg.channel.send(f"Role {rolename} has been created.")
    
async def roledel(msg):
    if discord.utils.get(msg.author.roles, name="Head Admin") is None:
        await msg.channel.send("You can't do that.")
    else:
        rolename = msg.content.split(" ")[1]
        await msg.guild.create_role(name=str(rolename))
        await msg.channel.send(f"Role has been deleted.")

async def addrole(msg):
    rol = msg.content
    rolemsg = rol.replace("=addrole ", "")
    role = discord.utils.get(msg.guild.roles , name=str(rolemsg))
    if role in msg.author.roles:
        await msg.channel.send(f"{msg.author.mention} already has {role}")
    else:
        await msg.author.add_roles(role)
        await msg.channel.send(f"{role} has been added to {msg.author.mention}")
   
async def delrole(msg):
    rol = msg.content
    rolemsg = rol.replace("=delrole ", "")
    role = discord.utils.get(msg.guild.roles , name=str(rolemsg))
    if role not in msg.author.roles:
        await msg.channel.send(f"{msg.author.mention} doesn't have {role}")
    else:
        await msg.author.remove_roles(role)
        await msg.channel.send(f"{role} has been removed from {msg.author.mention}")
        
        
    