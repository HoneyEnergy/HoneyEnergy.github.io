import discord
from discord.ext import commands
#from help import indexhelp
from dotenv import load_dotenv
import os
load_dotenv('.env')
TOKEN = os.getenv('TOKEN')
bot = commands.Bot(command_prefix='$', intents= discord.Intents.all())

@bot.event
async def on_ready():
        print("---------------------------------------")
        print("")
        print("bot is online!")
        print("")
        print("---------------------------------------")
@bot.event
async def on_member_update(usr_before, usr_after):
    if bot.user.status == discord.Status.online:
        print("---------------------------------------")
        print("")
        print("bot is online!")
        print("")
        print("---------------------------------------")
@bot.command()
async def info(ctx):
    await ctx.send("this bot is made by  HoneyEnergy.github.io")
    await ctx.send("for info or to see the source code vist our GitHub https://github.com/HoneyEnergy/HoneyEnergy.github.io/tree/main/discordbot")
    return
@bot.command()
async def web(ctx):
    await ctx.send("JATO'S website https://honeyenergy.github.io")
    return
@bot.command()
async def jthelp(ctx):
    await ctx.send(f"""
`$info`
`$web`
`$donate`

**New Commands and other stuff commning soon**
**If you want to help us please vist https://github.com/HoneyEnergy/HoneyEnergy.github.io Thank YOU :heart: **
{ctx.author.mention}
""")
    return
@bot.command()
async def donate(ctx):
    await ctx.send(f"""
Bitcion: bc1q49m86y3qd8ts6uqnldhjeez65lyrqhjzqvrtny
Monero: 43vBCrhEBN8ZHZsUQ6WAFAdjHUsbzo6H293E7DfpETRkZYttGFXfSFrUaRS62oYQE7AihVT3E6BMWQfw1FL7AEVuFCfeC3s
""")
bot.run(TOKEN)
