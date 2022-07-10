from contextvars import Token
import discord
from discord.ext import commands
import json
import random

# client is the bot initiation
client = commands.Bot(command_prefix = ['.'])
with open('config.json','r') as token:
    TOKEN = json.load(token)
        
# Start statement
@client.event
async def on_ready():
    print('[ED] Bot ready')

@client.command()
async def fruit(ctx):
    await ctx.send(random.choice(['🍇','🍈','🍋','🥭','🥝','🍒','🍓','🍏','🥑','🍍','🍌','🍎']))

@client.command(aliases=['bal'])
async def balance(ctx):
    user = ctx.author
    await open_account(ctx.author)
    users = await get_bank_data()
    
    wallet_amt = users[str(user.id)]['wallet']
    bank_amt = users[str(user.id)]['bank']
    
    em = discord.Embed(title=f"{ctx.author.name}'s balance",color = discord.Color.teal())
    em.add_field(name='Wallet',value=wallet_amt)
    em.add_field(name='Bank',value=bank_amt)
    await ctx.send(embed=em)
    
@client.command()
async def beg(ctx):
    user = ctx.author
    await open_account(ctx.author)
    users = await get_bank_data()

    earned = random.randint(0,167)
    await ctx.send(f'> Someone gave you {earned} coins')
    users[str(user.id)]['wallet'] += earned
    
    with open('mainbank.json','w') as f:
        users = json.dump(users,f)
        
async def open_account(user):
    users = await get_bank_data()
        
    if str(user.id) in users:
            return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]['wallet'] = 6
        users[str(user.id)]['bank'] = 52
            
    with open('mainbank.json','w') as f:
        users = json.dump(users,f)
    return True

async def get_bank_data():
    with open('mainbank.json','r') as f:
        users = json.load(f)
    return users

client.run(TOKEN['token'])