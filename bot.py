

# bot.py


'''
import discord
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )




    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

client.run(TOKEN)

'''
import discord
from discord.ext import tasks
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=discord.Intents.default())

for guild in client.guilds:
    for channel in guild.channels:
        print(channel.name)



@tasks.loop(seconds=10.0, count=10000)
async def printshit():
    print("You are cool")
    client.get_all_channels()

async def my_setup_hook():
    printshit.start()

client.setup_hook = my_setup_hook

client.run(TOKEN)




