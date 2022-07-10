import discord
from discord.ext import commands

# TOKEN controls the bot, do not share it / client is the bot initiation
TOKEN = "OTUwMTIxMTE1NTU5MjkzMDY4.G-TeiK.bzw7HwBKnXZvyYdk9mIqZmW8iSPxHdnVwbFyQQ"
client = commands.Bot(command_prefix = ['.'])

# Start statement
@client.event
async def on_ready():
    print('[ED] Bot ready')
    
client.run(TOKEN)