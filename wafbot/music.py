#music/voice channel cmds
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

intents = discord.Intents.default()
client = discord.Client()

song_queue = []
queuetoshow = []
requestedby = []
songdurations =[]
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    
def repeat(guild, voice):
    
        voice.play(discord.FFmpegPCMAudio("song.webm"), after=lambda e: repeat(guild, voice))
        voice.is_playing()

def play_next(client, msg):
    voice = get(client.voice_clients, guild=msg.guild)
    if len(song_queue) > 1:
        del song_queue[0]
        del queuetoshow[0]
        del songdurations[0]
        del requestedby[0]
        voice.play(discord.FFmpegPCMAudio(song_queue[0], **FFMPEG_OPTIONS), after=lambda e: play_next(client, msg))
        voice.is_playing()

@client.event
async def join(client, msg):
    
    channel = msg.author.voice.channel
    await channel.connect()
    await msg.channel.send(f"Bot joined `{channel}`!")
    await msg.add_reaction("👍")

async def leave(client, msg):
    
    channel = msg.author.voice.channel
    song_queue.clear()
    await msg.guild.voice_client.disconnect()
    await msg.channel.send(f"Bot left `{channel}`!")
    await msg.add_reaction("👍")

async def play(client, msg):
    voice = discord.utils.get(client.voice_clients, guild=msg.channel.guild)
    if voice is None:
        channel = msg.author.voice.channel
        await channel.connect()
        await msg.channel.send(f"Bot joined `{channel}`!")
    search = msg.content.replace("=play ", "")
    query_string = urllib.parse.urlencode({'search_query': search})
    htm_content = urllib.request.urlopen(
        'http://www.youtube.com/results?' + query_string)
    search_results = re.findall(r'/watch\?v=(.{11})',
                                htm_content.read().decode())
    song = str('http://www.youtube.com/watch?v=' + search_results[0])
    with youtube_dl.YoutubeDL(YDL_OPTIONS ) as ydl:
        info = ydl.extract_info(f"ytsearch:{search}", download=False)['entries'][0]
    
    duration = float(info['duration'])
    duration = duration / float(60)
    duration = int(duration) 
    song_queue.append(song)
    queuetoshow.append(str(info['title']))
    songdurations.append(str(duration))
    requestedby.append(str(msg.author))
    voice = discord.utils.get(client.voice_clients, guild=msg.channel.guild)
    if voice.is_playing():
        await msg.channel.send("Added to queue!")
    else:
        with youtube_dl.YoutubeDL(YDL_OPTIONS ) as ydl:
            ydl.download([song])
        voice.stop()
        user = client.user
        await user.edit(deafen=True)
        for file in os.listdir("./"):
            if file.endswith(".webm"):
                os.rename(file, "song.webm")
                voice.play(discord.FFmpegPCMAudio("song.webm"), after=lambda e: play_next(client, msg))
                embed=discord.Embed(title=f"Now Playing!", url=song, description=info['title'], color=0x06f459)
                embed.set_thumbnail(url=info['formats'][0]['url'])
                embed.add_field(name=f"`Length`-", value=f"{duration} minutes", inline=False)
                embed.add_field(name="`Requested by-`", value=f"{msg.author}", inline=False)
                embed.set_footer(text="Contact STUFFEDWAFFLES8367 for more info on bot")
                await msg.channel.send(embed=embed)
                await msg.add_reaction("👍")
           
async def yoink(msg):
    embed=discord.Embed(title=f"Currently Playing Song- {queuetoshow[0]}", url=song_queue[0], description=f"Reqested by- {requestedby[0]}", color=0x06f459)
    await msg.channel.send(embed=embed)
            
            
async def queue(msg):
    
    if song_queue == []:
        await msg.channel.send("Nothing in queue!")
    else:
        embed=discord.Embed(title=f"1. Currently Playing Song-{queuetoshow[0]}", description="Rest Of Queue-", color=0x06f459)
        if len(song_queue) > 1:
            embed.add_field(name=f"2. {queuetoshow[1]}", value=f"Length-{songdurations[1]} minutes, Requested by- {requestedby[2]}", inline=False)
        if len(song_queue) > 2:
            embed.add_field(name=f"3. {queuetoshow[2]}", value=f"Length-{songdurations[2]} minutes, Requested by- {requestedby[2]}", inline=False)
        await msg.channel.send(embed=embed)

async def pause(client, msg):
    voice: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=msg.author.guild)

    voice.pause()
    await msg.add_reaction("👍")

async def resume(client, msg):
    voice: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=msg.author.guild)

    voice.resume()
    await msg.add_reaction("👍")

async def clear(client, msg):
    voice: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=msg.author.guild)
    for file in os.listdir("./"):
            if file.endswith(".webm"):
                os.remove(file)
    voice.stop()
    song_queue.clear()
    queuetoshow.clear()
    await msg.add_reaction("👍")

async def loop(client, msg):
    voice = discord.utils.get(client.voice_clients, guild=msg.channel.guild)
    guild = msg.guild
    voice.pause()
    voice.play(discord.FFmpegPCMAudio("song.webm"), after=lambda e: repeat(guild, voice))
    await msg.channel.send("Looping song!")
    await msg.add_reaction("👍")

async def remove(client, msg):
    
    indexx = msg.content.split(" ")[1]
    sum = float(indexx) - float(1)
    index = int(sum)
    del song_queue[index]
    del queuetoshow[index]
    del songdurations[index]
    del requestedby[index]
    await msg.channel.send("Removed song!")
    await msg.add_reaction("👍")

async def stop(client, msg):
    voice = discord.utils.get(client.voice_clients, guild=msg.channel.guild)
    voice.stop()
    await msg.channel.send("Song stopped.")


