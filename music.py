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
client = discord.Client()
bot = commands.Bot


players = {}

queues = []

def check_queue(id):
    if queues[id] != []:
        player = queues[id].pop(0)
        players[id] = player
        player.start()

@client.event
async def join(client, msg):
    guild = msg.channel.guild
    channel = msg.author.voice.channel
    await channel.connect()
    await msg.channel.send("Bot joined `" + str(channel) + "`!")
    await msg.add_reaction("👍")


async def leave(client, msg):
    guild = msg.channel.guild
    channel = msg.author.voice.channel
    voice = msg.author.voice.channel
    await msg.guild.voice_client.disconnect()
    await msg.channel.send("Bot left `" + str(channel) + "`!")
    await msg.add_reaction("👍")
   

async def play(client, msg):
    guild = msg.channel.guild
    channel = msg.author.voice.channel
    urlfrommsg = msg.content.split(" ")[1:]
    url = str(urlfrommsg)

    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=msg.author.guild)

    
    with YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url[2:-2], download=False)
    URL = info['formats'][0]['url']

    if voice.is_playing is False:
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after=lambda : check_queue(guild.id))
        voice.is_playing() = True

    else:
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after=lambda : check_queue(guild.id))
        voice.is_playing()
        if guild.id in queues:
            queues[guild.id].append(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after=lambda : check_queue(guild.id))
        else:
            queues[guild.id] = [url]
        await msg.add_reaction("👍")
        await msg.channel.send("Added to queue!")
    
    
async def pause(client, msg):
    voice: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=msg.author.guild)

    voice.pause()
    await msg.add_reaction("👍")


async def resume(client, msg):
    voice: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=msg.author.guild)

    voice.resume()
    await msg.add_reaction("👍")







