import discord
from discord.ext import commands
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)



@bot.command()
async def recicla(ctx):
    reciclar = os.listdir('reciclar')
    
    with open(f'reciclar/{random.choice(reciclar)}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("")
