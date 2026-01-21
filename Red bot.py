import discord
import os
import random

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'FBI FBI OPEN UP!{bot.user} HERE!')

@bot.command()
async def facts(ctx):
    facts = [
        "The United States produces 30% of the world’s waste and uses 25 % of the worlds natural resources",
        "Around 1000 children die in India every year due to diseases caused by polluted water",
        "5000 people die every day as a result of drinking unclean water.",
    ] 

    
    await ctx.send(random.choice(facts))

@bot.command()
async def hello(ctx):
    await ctx.send(f'☭ Hello there! Im the red robot! ☭')

bot.run("ToKeN")
