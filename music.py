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
client = discord.Client()
bot = commands.Bot

@client.event
async def join(client, msg):
    guild = client.get_guild(762718463575064636)
    channel = msg.author.voice.channel
    await channel.connect()
    await msg.channel.send("Bot joined `" + str(channel) + "`!")
    await msg.add_reaction("👍")


async def leave(client, msg):
    guild = client.get_guild(762718463575064636)
    channel = msg.author.voice.channel
    voice = msg.author.voice.channel
    await msg.guild.voice_client.disconnect()
    await msg.channel.send("Bot left `" + str(channel) + "`!")
    await msg.add_reaction("👍")
   

async def play(client, msg):
    guild = client.get_guild(762718463575064636)
    channel = msg.author.voice.channel
    voice_client = await client.connect()
    url = msg.content.split(" ")[1]
    player = await voice_client.create_ytdl_player(url)
    player.start()



    