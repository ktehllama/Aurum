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
async def balance(ctx,member:discord.Member="SpecNone"):
    if member == "SpecNone":
        user = ctx.author
        await open_account(user)
        users = await get_bank_data()
        
        em = discord.Embed(title=f"{user.name}'s balance",color = discord.Color.teal())
        em.add_field(name='Wallet',value=users[str(user.id)]['wallet'])
        em.add_field(name='Bank',value=users[str(user.id)]['bank'])
        await ctx.reply(embed=em, mention_author=False)
    elif member != "SpecNone":
        user = member
        await open_account(user)
        users = await get_bank_data()
        
        em = discord.Embed(title=f"{user.name}'s balance",color = discord.Color.teal())
        em.add_field(name='Wallet',value=users[str(user.id)]['wallet'])
        em.add_field(name='Bank',value=users[str(user.id)]['bank'])
        await ctx.reply(embed=em, mention_author=False)
    
@client.command()
@commands.cooldown(1,10,commands.BucketType.user)
async def beg(ctx):
    user = ctx.author
    await open_account(user)
    users = await get_bank_data()

    earned = random.randint(0,167)
    await ctx.send(f'> Someone gave you {earned} coins')
    users[str(user.id)]['wallet'] += earned
    
    with open('mainbank.json','w') as f:
        users = json.dump(users,f)
@beg.error
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandOnCooldown):
        errors = ["A1","A2","A3","A4"]
        errorem = discord.Embed(title=random.choice(errors),description="You're on a cooldown for this command, wait `{:.2f}` seconds to use it again".format(error.retry_after),color=discord.Colour.from_rgb(71,153,230))
        await ctx.reply(embed=errorem,mention_author=False)
        
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