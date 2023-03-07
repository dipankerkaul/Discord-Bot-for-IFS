
# bot.py
# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = "MTA4MjIxMjMwOTM4NjE0OTg5OQ.G43b07.eENdFKz2DZCDHSxk36zv0udn0QifQ1qFEvlnWY"

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)

