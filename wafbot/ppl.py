#twitch channels n stuff, custom user commands
import discord
import asyncio
from discord.utils import get
import praw 
client = discord.Client()

async def waffle(msg):
    embed=discord.Embed(title="Waffle time!", url="https://belgian-waffle.recipes/make-perfect-stuffed-waffles/", description="How to make the perfect Belgian Stuffed Waffles! Click title for recipie!", color=0x9131f2)
    embed.set_author(name="STUFFEDWAFFLES")
    embed.set_image(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fkirbiecravings.com%2Fwp-content%2Fuploads%2F2014%2F06%2Fstuffed-nutella-waffles-31.jpg&f=1&nofb=1")
    embed.set_footer(text="Contact STUFFEDWAFFLES8367 for more information on waffles")
    await msg.channel.send(embed=embed)
    
async def jedi(msg):
    embed=discord.Embed(title="Jedi_JoeYT's youtube channel!", description="(UNSOUPSCRIBE FOR FREE COOKIE)", color=0xe31c30)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/727612091187462244/9ad60611152439dd8c4a08e8e93b0bf9.webp?size=256")
    embed.add_field(name="Channel- ", value="https://www.youtube.com/channel/UCmzcr6ouQa8RvzV2vEP0HfA", inline=False)
    embed.set_footer(text="Contact Jedi_JoeYT7387 for cookie")
    await msg.channel.send(embed=embed)

async def para(msg):
    embed=discord.Embed(title="Paracreeper21!", url="https://www.youtube.com/watch?v=cPJUBQd-PNM", description="Redstone Master and Minecraft Meme Creator", color=0x017409)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette.wikia.nocookie.net%2Fborderlands%2Fimages%2F3%2F36%2FCreeper_2.jpg%2Frevision%2Flatest%3Fcb%3D20180125164446&f=1&nofb=1")
    embed.set_footer(text="Contact paracreeper218768 to make giant redstone contraptions")
    await msg.channel.send(embed=embed)
        
async def ched(msg):
    embed=discord.Embed(title="Chedboy2_0- new twitch and YT channel!", description="sub for free cookie :D! Streams minecraft, overwatch, and maybe even rocket league!", color=0x0088ff)
    embed.set_thumbnail(url="https://static-cdn.jtvnw.net/jtv_user_pictures/fb94f1c0-8ed8-4a6d-8165-8a5456f01234-profile_image-70x70.png")
    embed.add_field(name="Twitch Channel!-", value="https://www.twitch.tv/chedboy2_0", inline=False)
    embed.add_field(name="YT channel-", value="https://www.youtube.com/channel/UCcaaF00E_KrB9y7BO_OEyfQ?view_as=subscriber", inline=False)
    embed.set_footer(text="Contact Chedboy2_0 5365 for cookie after subbing(we love ya ched)")
    await msg.channel.send(embed=embed)
    
async def rick(msg):
    await msg.delete()
    await msg.channel.send(file=discord.File('rick.gif'))
    
   
    
async def destiny(msg):
    embed=discord.Embed(title="Destiny!", url=("https://www.twitch.tv/destinyd0424"), description="twitch channel! click title for link!", color=0xff24ba)
    embed.set_footer(text="Contact destiny7112 for more information")
    await msg.channel.send(embed=embed)
    
async def daky(msg):
    embed=discord.Embed(title="Daky the child stabber!", url="https://www.twitch.tv/dak_lol", description="twitch channel(and YT but he made me remove it) \nclick the title for link to channel", color=0xf5ed00)
    embed.set_thumbnail(url="https://static-cdn.jtvnw.net/jtv_user_pictures/5b9b0d7e-af1f-4962-a163-06b6f0b210de-profile_image-70x70.png")
    embed.set_footer(text="Contact Daklol7493 for more information about ducks")
    await msg.channel.send(embed=embed)
    
async def aqwuah(msg):
    embed=discord.Embed(title="Aqwuah's twitch channel!", url="https://www.twitch.tv/aqwuah_", description="click the title for a link to the channel!", color=0x00f5f1)
    embed.set_footer(text="Contact aqwuah9526 for more information")
    await msg.channel.send(embed=embed)