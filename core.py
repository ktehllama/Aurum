import discord
from discord.ext import commands
import json
import random
import asyncio

# client is the bot initiation
client = commands.Bot(command_prefix = ['.'])
with open('config.json','r') as token:
    TOKEN = json.load(token)
    
# Start statement
@client.event
async def on_ready():
    print('[ED] Bot ready')
    
moni = "<a:moni:950492202541408406>"
bruh = "<a:bruh:950550513697574942>"
printer = "<a:printer:950491986606043196>"
fatkid = "<:fatkid:950761893583278212>"
skull = "<a:skull:950876386250326037>"

@client.command(aliases=['kys'])
async def end(ctx):
    author = ctx.message.author
    if author.id == 680154732567855259:
        await ctx.send('> **Terminated program**')
        exit(1)

@client.event #Replace 'client' with whatever neccesary
async def on_command_error(ctx, error):
    await ctx.send(error)

@client.command()
async def fruit(ctx):
    await ctx.send(random.choice(['🍇','🍈','🍋','🥭','🥝','🍒','🍓','🍏','🥑','🍍','🍌','🍎','🍉','🍐']))

@client.command(aliases=['bal'])
async def balance(ctx,member:discord.Member="SpecNone"):
    if member == "SpecNone":
        user = ctx.author
        await open_account(user)
        users = await get_bank_data()
        
        em = discord.Embed(title=f"{user.name}'s balance",color = discord.Color.teal())
        em.add_field(name='Wallet',value="`⌬ {:,}`".format(users[str(user.id)]['wallet']))
        em.add_field(name='Bank',value="`⌬ {:,}`".format(users[str(user.id)]['bank']))
        await ctx.reply(embed=em, mention_author=False)
    elif member != "SpecNone":
        user = member
        await open_account(user)
        users = await get_bank_data()
        
        em = discord.Embed(title=f"{user.name}'s balance",color = discord.Color.teal())
        em.add_field(name='Wallet',value="`⌬ {:,}`".format(users[str(user.id)]['wallet']))
        em.add_field(name='Bank',value="`⌬ {:,}`".format(users[str(user.id)]['bank']))
        await ctx.reply(embed=em, mention_author=False)
        
@client.command()
@commands.cooldown(1,10,commands.BucketType.user)
async def beg(ctx):
    user = ctx.author
    await open_account(user)
    users = await get_bank_data()
    
    beg_weights = random.choices(['Yes','No'], weights=(63,47), k=2)
    beg_rates = random.choice(beg_weights)

    if beg_rates == 'Yes':
        earned = random.randint(1,120)
        await ctx.reply(f'> Someone gave you `⌬ {earned}` coins', mention_author=False)
        users[str(user.id)]['wallet'] += earned
    elif beg_rates == 'No':
        await ctx.reply(f'> No one wanted to give you money {skull}', mention_author=False)
    
    with open('mainbank.json','w') as f:
        users = json.dump(users,f)
@beg.error
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandOnCooldown):
        errors = ["wait a moment I'm currently hacking into your router","be patient meth doesn't cook that fast","i'm underpaid please wait for the cooldown"]
        errorem = discord.Embed(title=random.choice(errors),description="You're on a cooldown for this command, wait `{:.2f}` seconds to use it again".format(error.retry_after),color=discord.Colour.from_rgb(71,153,230))
        await ctx.reply(embed=errorem,mention_author=False,delete_after=4)

# @client.command()
# @commands.cooldown(1, 30, commands.BucketType.user)
# async def test(ctx, command=None):
#     if command is None:
#         await ctx.send('I want this to ignore cooldown')
#         slots.reset_cooldown(ctx)
#     elif command.lower() == '2':
#         await ctx.send('I want this to have a Cooldown') 

@client.command(aliases = ['slot'])
@commands.cooldown(1,20,commands.BucketType.user)
async def slots(ctx, amount=None):
        user = ctx.message.author
        await open_account(user)
        if amount == None:
            amount = 0
            wdEmbed = discord.Embed(title=f"{user.name}...",description='Please specify the amount of `⌬` you want to bet',color = discord.Color.from_rgb(217,55,52))
            await ctx.reply(embed=wdEmbed, mention_author=False)
            slots.reset_cooldown(ctx)
            return
            
        bal = await update_bank(user)
        
        amount = int(amount)
        if amount > bal[0]:
                wdEmbed = discord.Embed(title=f"{user.name}...",description='You do not have `⌬ {:,}` to bet (Money must be in your wallet)'.format(amount),color = discord.Color.from_rgb(217,55,52))
                await ctx.reply(embed=wdEmbed, mention_author=False)
                slots.reset_cooldown(ctx)
                return
        elif amount < 0:
                wdEmbed = discord.Embed(title=f"{user.name}...",description='The amount of `⌬` you want to bet must be positive',color = discord.Color.from_rgb(217,55,52))
                await ctx.reply(embed=wdEmbed, mention_author=False)
                slots.reset_cooldown(ctx)
                return
        elif amount == 0:
                wdEmbed = discord.Embed(title=f"{user.name}...",description='The amount of `⌬` you want to bet must be above zero',color = discord.Color.from_rgb(217,55,52))
                await ctx.reply(embed=wdEmbed, mention_author=False)
                slots.reset_cooldown(ctx)
                return
        elif amount == 1:
                wdEmbed = discord.Embed(title=f"{user.name}...",description='The amount of `⌬` you want to bet must be above 1',color = discord.Color.from_rgb(217,55,52))
                await ctx.reply(embed=wdEmbed, mention_author=False)
                slots.reset_cooldown(ctx)
                return
        
        
        slt_list = ['🍇','🍉','🥝','💣','🥐']
        for li in range(3):
            slt_choices = random.choices(slt_list, weights=[12.1,12.2,12.3,14.7,12.4],k=3)
        
        score = 0
        for ri in range(5):
            if slt_choices.count('💣') == 2:
                score -= 1
            else:    
                if slt_choices.count(slt_list[ri]) == 2:
                    score += 1
                    
            if slt_choices.count('💣') == 3:
                score -= 1
            else:    
                if slt_choices.count(slt_list[ri]) == 3:
                    score += 2
                
        outcomemessage = 'NaN'
        lastmsg = 'NaN'
        amwon = 0
        if score == 0:
            await update_bank(user,-1*amount)
            outcomemessage = 'You **lost**'
            lastmsg = '(No matches)'
            amwon = 1*amount
        if score == 1:
            await update_bank(user,2*amount)
            outcomemessage = 'You **won**'
            lastmsg = '(2 matches)'
            amwon = 2*amount
        if score == 2:
            await update_bank(user,4*amount)
            outcomemessage = 'You **won**'
            lastmsg = '(3 matches)'
            amwon = 4*amount
        if score == -5:
            await update_bank(user,-3*amount)
            outcomemessage = 'You **lost**'
            lastmsg = '(Bomb matches)'
            amwon = 3*amount
            
        users = await get_bank_data() 
        
        editEmbed = discord.Embed(title=f"{user.name} | Slots",description='You bet `⌬ {:,}`\n\n**[** {} `|` {} `|` {} **]**\n\n. . .'.format(amount,random.choice(slt_list),random.choice(slt_list),random.choice(slt_list)),color = discord.Color.from_rgb(116,237,100))
        ebe = await ctx.reply(embed=editEmbed, mention_author=False)
        for randrange in range(4):
            sEmbed = discord.Embed(title=f"{user.name} | Slots",description='You bet `⌬ {:,}`\n\n**[** {} `|` {} `|` {} **]**\n\n. . .'.format(amount,random.choice(slt_list),random.choice(slt_list),random.choice(slt_list)),color = discord.Color.from_rgb(116,237,100))
            await ebe.edit(embed=sEmbed)
            await asyncio.sleep(0.1)
        
        users = await get_bank_data() 
        wallet_amt = users[str(user.id)]['wallet']
        
        em_color = [116,237,100]
        if outcomemessage == "You **lost**":
            em_color = [219,69,65]
        
        finalEmbed = discord.Embed(
            title=f"{user.name} | Slots",
            description='You bet `⌬ {:,}`\n\n{}\n\n{} `⌬ {:,}` *{}*'.format(amount,str(slt_choices).replace('[','**[**').replace(']',' **]**').replace("'",'').replace(',',' `|` '),outcomemessage,amwon,lastmsg),
            color = discord.Color.from_rgb(em_color[0],em_color[1],em_color[2])
        )
        finalEmbed.add_field(name='Wallet value:',value='`⌬ {:,}`'.format(wallet_amt), inline=False)
        await ebe.edit(embed=finalEmbed)
@slots.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        errors = ["wait a moment I'm currently hacking into your router","be patient meth doesn't cook that fast","i'm underpaid please wait for the cooldown"]
        errorem = discord.Embed(title=random.choice(errors),description="You're on a cooldown for this command, wait `{:.2f}` seconds to use it again".format(error.retry_after),color=discord.Colour.from_rgb(71,153,230))
        await ctx.reply(embed=errorem,mention_author=False,delete_after=4)      
        
@client.command(aliases=['with'])
async def withdraw(ctx,amount = None):
    user = ctx.author
    users = await get_bank_data()
    await open_account(ctx.author)

    if amount == None:
      await ctx.reply(f'you need to enter an amount to withdraw smh',mention_author=False) 
      return
    bal = await update_bank(ctx.author)
    
    bank_amt = users[str(user.id)]["bank"]
    if amount == "all":
          if bank_amt<=0:
            await ctx.reply(f'thats impossible lmao, theres nothing to withdraw',mention_author=False) 
            return
          await update_bank(ctx.author,bank_amt)
          await update_bank(ctx.author,-1*bank_amt,"bank")
          emsu = discord.Embed(title="Withdraw",description="You withdrew `⌬ {:,}`".format(bank_amt),color=discord.Colour.from_rgb(237,240,240))
    else:
        amount = int(amount)
        if amount>bal[1]:
            await ctx.reply(f'you dont have enough money to withdraw that amount lol',mention_author=False) 
            return
        if amount<=0:
            await ctx.reply(f'withdraw an amount of money greater than 0',mention_author=False) 
            return

        await update_bank(ctx.author,amount)
        await update_bank(ctx.author,-1*amount,"bank")
        emsu = discord.Embed(title="Withdraw",description="You withdrew `⌬ {:,}`".format(amount),color=discord.Colour.from_rgb(237,240,240))
    
    users = await get_bank_data()
    emsu.add_field(name="Current wallet balance",value="`⌬ {:,}`".format(users[str(user.id)]["wallet"]))
    emsu.add_field(name="Current bank balance",value="`⌬ {:,}`".format(users[str(user.id)]["bank"]))
    await ctx.reply(embed=emsu,mention_author=False)
    
@client.command(aliases=['dep'])
async def deposit(ctx,amount = None):
    user = ctx.author
    users = await get_bank_data()
    await open_account(ctx.author)

    if amount == None:
        await ctx.reply(f'you need to enter an amount to deposit smh',mention_author=False) 
        return
    bal = await update_bank(ctx.author)
    
    wallet_amt = users[str(user.id)]["wallet"]
    if amount == "all":
      if wallet_amt<=0:
            await ctx.reply(f'thats impossible lmao, theres nothing to deposit',mention_author=False) 
            return
      await update_bank(ctx.author,-1*wallet_amt)
      await update_bank(ctx.author,wallet_amt,"bank")
      emsu = discord.Embed(title="Deposit",description="You deposited `⌬ {:,}`".format(wallet_amt),color=discord.Colour.from_rgb(237,240,240))
    else:
      amount = int(amount)
      if amount>bal[0]:
        await ctx.reply(f'you dont have enough money to deposit that amount lol',mention_author=False) 
        return
      if amount<=0:
        await ctx.reply(f'deposit an amount of money greater than 0',mention_author=False) 
        return
      
      await update_bank(ctx.author,-1*amount)
      await update_bank(ctx.author,amount,"bank")
      emsu = discord.Embed(title="Deposit",description="You deposited `⌬ {:,}`".format(amount),color=discord.Colour.from_rgb(237,240,240))
      
    users = await get_bank_data()
    emsu.add_field(name="Current wallet balance",value="`⌬ {:,}`".format(users[str(user.id)]["wallet"]))
    emsu.add_field(name="Current bank balance",value="`⌬ {:,}`".format(users[str(user.id)]["bank"]))
    await ctx.reply(embed=emsu,mention_author=False)
  
@client.command(aliases=['give','transfer'])
@commands.cooldown(5,10,commands.BucketType.user)
async def send(ctx,member:discord.Member="SpecNone",amount = None):
    user = ctx.author
    users = await get_bank_data()
    await open_account(ctx.author)
    if member != "SpecNone":
      if member == user:
        await ctx.reply(f"you can't send yourself money {skull}", mention_author=False)
        return
      else:
        await open_account(member)
    else:
        await ctx.reply(f'you need to enter an person you want to give money to lmao',mention_author=False) 
        return

    if amount == None:
      await ctx.reply(f'you need to enter an amount to send smh',mention_author=False)  
      return
        
    bal = await update_bank(ctx.author)
    amount = int(amount)
    if amount>bal[1]:
      await ctx.reply("either you aren't rich enough to give `⌬ {:,}`, or you forgot to deposit it in your bank before giving it {}".format(amount,fatkid),mention_author=False) 
      return
    if amount<=0:
      await ctx.reply(f'thats impossible lol, send an amount of money greater than 0',mention_author=False) 
      return

    await update_bank(ctx.author,-1*amount,"bank")
    await update_bank(member,amount,"bank")

    users = await get_bank_data()
    sendem = discord.Embed(title="Money sent",description="You sent `⌬ {:,}` to {} {}".format(amount,member.mention,moni),color=discord.Colour.from_rgb(188,206,219))
    sendem.set_footer(text='put those ⌬ to good use {}, or not, i dont care'.format(member.name))
    await ctx.reply(embed=sendem,mention_author=False)
@send.error
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandOnCooldown):
        errors = ["wait a moment I'm currently hacking into your router","be patient meth doesn't cook that fast","i'm underpaid please wait for the cooldown"]
        errorem = discord.Embed(title=random.choice(errors),description="You're on a cooldown for this command, wait `{:.2f}` seconds to use it again".format(error.retry_after),color=discord.Colour.from_rgb(71,153,230))
        await ctx.reply(embed=errorem,mention_author=False,delete_after=4)
        
@client.command(aliases = ['lb'])
async def leaderboard(ctx,x=5):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total, reverse=True)

    em = discord.Embed(title=f":trophy: Top {x} Richest People :trophy:", color = discord.Color.from_rgb(100,233,237))
    em.set_footer(text='This is based on wallet + bank value')
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = await client.fetch_user(id_)
        name = member.name
        em.add_field(name=f"*{index}*. {name}", value="`⌬ {:,}`".format(amt), inline=False)
        if index == x:
            break
        else:
            index += 1
    await ctx.reply(embed=em, mention_author = False)
        
#  -     -                
        
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

async def update_bank (user,change = 0,mode = 'wallet'):
    users = await get_bank_data() 

    users[str(user.id)][mode] += change 

    with open("mainbank.json","w") as f:
      json.dump(users,f) 
    bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
    return bal

async def get_bank_data():
    with open('mainbank.json','r') as f:
        users = json.load(f)
    return users

client.run(TOKEN['token'])