import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
@bot.command()
async def info(ctx):
    await ctx.send('This bot is created by HonyEnergy')
    await ctx.send('follow us on GitHub for more info https://github.com/HoneyEnergy/HoneyEnergy.github.io')
    return
bot.run('toke')
