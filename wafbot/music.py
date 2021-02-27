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
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
import urllib.parse, urllib.request, re
import wavelink
import swaglyrics
import re
import aiohttp
import praw 

intents = discord.Intents.default()
client = discord.Client()

song_queue = []
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    


def play_next(client, msg):
    voice = get(client.voice_clients, guild=msg.guild)
    if len(song_queue) > 1:
        del song_queue[0]
        voice.play(discord.FFmpegPCMAudio(song_queue[0][source], **FFMPEG_OPTIONS), after=lambda e: play_next(client, msg))
        voice.is_playing()


@client.event
async def join(client, msg):
    
    channel = msg.author.voice.channel
    await channel.connect()
    await msg.channel.send("Bot joined `" + str(channel) + "`!")
    await msg.add_reaction("👍")
    


async def leave(client, msg):
    
    channel = msg.author.voice.channel
    song_queue.clear()
    await msg.guild.voice_client.disconnect()
    await msg.channel.send("Bot left `" + str(channel) + "`!")
    await msg.add_reaction("👍")

async def video(msg):
    searchfrommsg = msg.content.split(" ")[1:]
    search = str(searchfrommsg)
    query_string = urllib.parse.urlencode({'search_query': search})
    htm_content = urllib.request.urlopen(
        'http://www.youtube.com/results?' + query_string)
    search_results = re.findall(r'/watch\?v=(.{11})',
                                htm_content.read().decode())
    url = str('http://www.youtube.com/watch?v=' + search_results[0])
    await msg.channel.send("Here is the first result to your search: " + url)
   

async def play(client, msg):
    voice = discord.utils.get(client.voice_clients, guild=msg.channel.guild)
    searchf = msg.content
    searchfrommsg = searchf.replace("=play ", "")
    search = str(searchfrommsg)
    query_string = urllib.parse.urlencode({'search_query': search})
    htm_content = urllib.request.urlopen(
        'http://www.youtube.com/results?' + query_string)
    search_results = re.findall(r'/watch\?v=(.{11})',
                                htm_content.read().decode())
    song = str('http://www.youtube.com/watch?v=' + search_results[0])
    
    print (song)
    title = searchfrommsg
    song_queue.append(song)

    
    
    if voice is None:
        await msg.channel.send("Not in a vc!")

    if voice.is_playing():
        await msg.channel.send("Added to queue!")
    else:
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            ydl.download([song])
        

        for file in os.listdir("./"):
            if file.endswith(".webm"):
                os.rename(file, "song.webm")
                voice.play(discord.FFmpegPCMAudio("song.webm"), after=lambda e: play_next(client, msg))
                await msg.channel.send("Playing `" + title + "`!")
                await msg.add_reaction("👍")
            
                

async def queue(msg):
    
    if song_queue == []:
        await msg.channel.send("Nothing in queue!")
    else:
        embed=discord.Embed(title="Queue!(still in progress dont judge me)", description="Now Playing- " + str(song_queue)[2], color=0x06f459)
        embed.add_field(name="Rest of queue-", value=str(song_queue)[2:], inline=False)
        embed.set_footer(text="Contact STUFFEDWAFFLES for more info on bot")
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
                os.remove("song.webm")
    voice.stop()
    song_queue.clear()
    await msg.add_reaction("👍")

async def loop(client, msg):
    voice = discord.utils.get(client.voice_clients, guild=msg.channel.guild)
    guild = msg.guild
    def repeat(guild, voice):
    
        voice.play(discord.FFmpegPCMAudio("song.webm"), after=lambda e: repeat(guild, VoiceClient))
        voice.is_playing()
    if voice.is_playing() is False:
        voice.play(discord.FFmpegPCMAudio("song.webm"), after=lambda e: repeat(guild, voice))
        await msg.channel.send("Looping song!")
        await msg.add_reaction("👍")

async def remove(client, msg):
    
    indexx = msg.content.split(" ")[1]
    sum = float(indexx) + float(1)
    index = int(sum)
    del song_queue[index]
    await msg.channel.send("Removed song!")
    await msg.add_reaction("👍")


async def stop(client, msg):
    voice = discord.utils.get(client.voice_clients, guild=msg.channel.guild)
    voice.stop()
    await msg.channel.send("Song stopped.")


