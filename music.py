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
    
def search(arg):
    try: requests.get("".join(arg))
    except: arg = " ".join(arg)
    else: arg = "".join(arg)
    with youtube_dl.YoutubeDL(YDL_OPTIONS ) as ydl:
        info = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
        
    return {'source': info['formats'][0]['url'], 'title': info['title']}

def play_next(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    if len(song_queue) > 1:
        del song_queue[0]
        voice.play(discord.FFmpegPCMAudio(song_queue[0], **FFMPEG_OPTIONS), after=lambda e: play_next(ctx))
        voice.is_playing()


@client.event
async def join(client, msg):
    
    channel = msg.author.voice.channel
    await channel.connect()
    await msg.channel.send("Bot joined `" + str(channel) + "`!")
    await msg.add_reaction("👍")
    
    
    voice = get(client.voice_clients, guild=msg.channel.guild)
    
    voice.play(discord.FFmpegPCMAudio("/home/pi/waf bot/wafbot/Rick Astley - Never Gonna Give You Up (Video)-dQw4w9WgXcQ.webm"))
    await asyncio.sleep(10)
    voice.pause()
    


async def leave(client, msg):
    
    channel = msg.author.voice.channel
    
    await msg.guild.voice_client.disconnect()
    await msg.channel.send("Bot left `" + str(channel) + "`!")
    await msg.add_reaction("👍")

async def url(msg):
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
    voice = get(client.voice_clients, guild=msg.channel.guild)
    
    voice.play(discord.FFmpegPCMAudio("/home/pi/waf bot/wafbot/Rick Astley - Never Gonna Give You Up (Video)-dQw4w9WgXcQ.webm"))
    voice.is_playing()
    
    
    

       
    
        
        
    


async def pause(client, msg):
    voice: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=msg.author.guild)

    voice.pause()
    await msg.add_reaction("👍")


async def resume(client, msg):
    voice: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=msg.author.guild)

    voice.resume()
    await msg.add_reaction("👍")







