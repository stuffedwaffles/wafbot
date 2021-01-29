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
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
import urllib.parse, urllib.request, re
import wavelink
intents = discord.Intents.default()
client = discord.Client()

song_queue = []
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
intents = discord.Intents.default()

song_queue = []

#define the bot
client = discord.Client(intents=intents)
bot = commands.Bot

async def on_message(msg):
    #language filter
    if msg.content.lower() in ["fuck", "shit"]:
        user = msg.author
        if user.bot == False:
            member = msg.author
            numb = random.randint(1,5)
            if numb == 2:
                await msg.channel.send("Hey " + member.mention + "! Watch your pooping language.")



def play_next(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    if len(song_queue) > 1:
        del song_queue[0]
        voice.play(discord.FFmpegPCMAudio(song_queue[0][source], **FFMPEG_OPTIONS), after=lambda e: play_next(ctx))
        voice.is_playing()
    
def search(arg):
    try: requests.get("".join(arg))
    except: arg = " ".join(arg)
    else: arg = "".join(arg)
    with youtube_dl.YoutubeDL(YDL_OPTIONS ) as ydl:
        info = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
        
    return {'source': info['formats'][0]['url'], 'title': info['title']}

    query1 = msg.content.split(" ")[1:]
    
    arg = str(query1)
    print (arg)

    channel = msg.author.voice.channel

    if channel:
        voice = get(client.voice_clients, guild=msg.channel.guild)
        song = search(arg)
        song_queue.append(song)
        print (song)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else: 
            voice = await channel.connect()

        if not voice.is_playing():
            voice.play(discord.FFmpegPCMAudio(song[0]['source'], **FFMPEG_OPTIONS), after=lambda e: play_next(ctx))
            voice.is_playing()
        else:
            await msg.channel.send("Added to queue")
    else:
        await msg.channel.send("You're not connected to any channel!")
    



    query1 = msg.content.split(" ")[1:]
    
    arg = str(query1)
    print (arg)

    channel = msg.author.voice.channel

    if channel:
        voice = get(client.voice_clients, guild=msg.channel.guild)
        song = search(arg)
        song_queue.append(song)
        print (song)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else: 
            voice = await channel.connect()
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                    ydl.download([song])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")
                voice.play(discord.FFmpegPCMAudio("song.mp3"))
                voice.is_playing()
            
            else:
                song_queue.remove(song)
                song_there = os.path.isfile("song.mp3")
                if song_there:
                    os.remove("song.mp3")