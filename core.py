import discord
from discord.ext import commands
import json
import random
import asyncio
import time

import traceback
import datetime

from help_cog import help_cog

# client is the bot initiation
client = commands.Bot(command_prefix = ['.'])
TOKEN = "BOT-TOKEN-HERE"
    
# Start statement
@client.event
async def on_ready():
    print('[ED] Bot ready')
    await client.change_presence(activity=discord.Game(name="message Teh llama#0014 for questions idk"))
    await client.add_cog(help_cog(client))
client.remove_command('help')

moni = "<a:moni:950492202541408406>"
bruh = "<a:bruh:950550513697574942>"
printer = "<a:printer:950491986606043196>"
fatkid = "<:fatkid:950761893583278212>"
skull = "<a:skull:950876386250326037>"
dollar = "<:dollar:996440567552680006>"

@client.command(aliases=['kys'])
async def end(ctx):
    author = ctx.message.author
    if author.id == 680154732567855259:
        await ctx.send('> **Terminated program**')
        exit(1)

# ERROR MODE
@client.event
async def on_command_error(ctx, error):
    await ctx.send(error)

@client.command()
async def fruit(ctx):
    await ctx.send(random.choice(['🍇','🍈','🍋','🥭','🥝','🍒','🍓','🍏','🥑','🍍','🍌','🍎','🍉','🍐']))
   
# EXPERIMENTAL
 
@client.command()
async def perms(ctx, user:discord.Member=None):
    if user == None:
        user = ctx.author
        
    await ctx.send('''```md\n# {}'s permissions\n\n{}\n```'''.format(user.name, "\n".join(p[0] for p in user.permissions_in(ctx.channel) if p[1])))
    
@client.command()
@commands.guild_only()
async def ba(ctx,amount):
    bala = 400
    max_amount = 500
    amount = int(amount)
    
    if amount > 500:
    
        subtract_amount = bala - max_amount
        amount_subtractive = amount - abs(subtract_amount)
        final_amount = amount - abs(amount_subtractive)
        
        await ctx.send(f'Amount left {subtract_amount}')
        await ctx.send(f'Amount to substract from AMOUNT {amount_subtractive}')
        await ctx.send(f'Final amount to add {abs(final_amount)}')
        
    else:
        await ctx.send('no need')

# EOS EXPER
        
@client.command(aliases=['bal'])
@commands.guild_only()
async def balance(ctx,member:discord.Member="SpecNone"):
    if member == "SpecNone":
        user = ctx.author
        await open_account(user)
        users = await get_bank_data()
        
        em = discord.Embed(title=f"{user.name}'s balance",color = discord.Color.teal())
        em.add_field(name='Wallet',value="`⌬ {:,}`".format(users[str(user.id)]['wallet']))
        em.add_field(name='Bank',value="`⌬ {:,} / ⌬ {:,}`".format(users[str(user.id)]['bank'],users[str(user.id)]['limit_bank']))
        await ctx.reply(embed=em, mention_author=False)
    elif member != "SpecNone":
        user = member
        await open_account(user)
        users = await get_bank_data()
        
        em = discord.Embed(title=f"{user.name}'s balance",color = discord.Color.teal())
        em.add_field(name='Wallet',value="`⌬ {:,}`".format(users[str(user.id)]['wallet']))
        em.add_field(name='Bank',value="`⌬ {:,} / ⌬ {:,}`".format(users[str(user.id)]['bank'],users[str(user.id)]['limit_bank']))
        await ctx.reply(embed=em, mention_author=False)
        
@client.command()
@commands.guild_only()
@commands.cooldown(1,15,commands.BucketType.user)
async def beg(ctx):
    user = ctx.author
    await open_account(user)
    users = await get_bank_data()
    
    beg_weights = random.choices(['Yes','No'], weights=(63,47), k=2)
    beg_rates = random.choice(beg_weights)

    if beg_rates == 'Yes':
        earned = random.randint(1,60)
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
        errorem = discord.Embed(title=random.choice(errors),description="You're on a cooldown for this command, wait `{:.0f}` seconds to use it again".format(error.retry_after),color=discord.Colour.from_rgb(71,153,230))
        await ctx.reply(embed=errorem,mention_author=False,delete_after=4)

@client.command(aliases = ['slot'])
@commands.guild_only()
@commands.cooldown(1,25,commands.BucketType.user)
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
        errorem = discord.Embed(title=random.choice(errors),description="You're on a cooldown for this command, wait `{:.0f}` seconds to use it again".format(error.retry_after),color=discord.Colour.from_rgb(71,153,230))
        await ctx.reply(embed=errorem,mention_author=False,delete_after=4)  

@client.command()
@commands.guild_only()
@commands.cooldown(1,50,commands.BucketType.user)
async def dice(ctx, amount=None):
        user = ctx.message.author
        await open_account(user)
        users = await get_bank_data() 
        if amount == None:
            amount = 0
            wdEmbed = discord.Embed(title=f"{user.name}...",description='Please specify the amount of `⌬` you want to bet',color = discord.Color.from_rgb(217,55,52))
            await ctx.reply(embed=wdEmbed, mention_author=False)
            dice.reset_cooldown(ctx)
            return
            
        bal = await update_bank(user)
        amount = int(amount)
        if amount > bal[0]:
                wdEmbed = discord.Embed(title=f"{user.name}...",description='You do not have `⌬ {:,}` to bet (Money must be in your wallet)'.format(amount),color = discord.Color.from_rgb(217,55,52))
                await ctx.reply(embed=wdEmbed, mention_author=False)
                dice.reset_cooldown(ctx)
                return
        elif amount < 0:
                wdEmbed = discord.Embed(title=f"{user.name}...",description='The amount of `⌬` you want to bet must be positive',color = discord.Color.from_rgb(217,55,52))
                await ctx.reply(embed=wdEmbed, mention_author=False)
                dice.reset_cooldown(ctx)
                return
        elif amount == 0:
                wdEmbed = discord.Embed(title=f"{user.name}...",description='The amount of `⌬` you want to bet must be above zero',color = discord.Color.from_rgb(217,55,52))
                await ctx.reply(embed=wdEmbed, mention_author=False)
                dice.reset_cooldown(ctx)
                return
        elif amount == 1:
                wdEmbed = discord.Embed(title=f"{user.name}...",description='The amount of `⌬` you want to bet must be above 1',color = discord.Color.from_rgb(217,55,52))
                await ctx.reply(embed=wdEmbed, mention_author=False)
                dice.reset_cooldown(ctx)
                return
        
        rand_dice = random.randint(1,10)
        bet_embed = discord.Embed(
                title = f"{user.name}, choose your bet",
                description = f'Type a number **`1-10`** below in `chat`',
            )
        bet_embed.set_footer(text='You have 30 seconds to choose ❕')
        bet_embed = await ctx.reply(embed=bet_embed, mention_author = False)
        
        nums_list = ['1','2','3','4','5','6','7','8','9','10']
        def check(m):
            return ctx.author == m.author
        try:
            bet_msg = await ctx.bot.wait_for('message', timeout=30.0, check=check)
            earned_coins = amount
            if bet_msg.content in nums_list:
                calc_range = rand_dice - int(bet_msg.content)
                calc = str(calc_range).replace('-','')
                
                editEmbed = discord.Embed(title=f"{user.name}, rolling the dice...",description='You bet `⌬ {:,}`\n\n🎲 🔹 🔹\n\n. . .'.format(amount))
                ebe = await bet_embed.edit(embed=editEmbed)

                sEmbed = discord.Embed(title=f"{user.name}, rolling the dice..",description='You bet `⌬ {:,}`\n\n🔹 🎲 🔹\n\n. . .'.format(amount))
                await bet_embed.edit(embed=sEmbed)
                await asyncio.sleep(0.1)
                sEmbed = discord.Embed(title=f"{user.name}, rolling the dice..",description='You bet `⌬ {:,}`\n\n🔹 🔹 🎲\n\n. . .'.format(amount))
                await bet_embed.edit(embed=sEmbed)
                await asyncio.sleep(0.1)
                
                if int(bet_msg.content) == rand_dice:
                    await bet_msg.delete()
                    earned_coins = 5*amount
                    bet_cr_embed = discord.Embed(
                        title = f"{user.name}, direct hit!",
                        description = f'You chose the number **`{bet_msg.content}`**\n\nThe dice rolled the number: **`{rand_dice}`** 🎲\n*You gained `⌬ {earned_coins}` coins*',
                        color = discord.Colour.from_rgb(242,198,78)
                    )
                    await bet_embed.edit(embed=bet_cr_embed, mention_author = False)
                    await update_bank(user,round(earned_coins))
                elif int(bet_msg.content) != rand_dice:
                    
                    if calc == '1':
                        earned_coins = round(2*amount)
                    elif calc == '2':
                        earned_coins = round(1.5*amount)
                    elif calc == '3':
                        earned_coins = round(-1*amount)
                    elif calc == '4':   
                        earned_coins = round(-1.8*amount)
                    elif calc == '5':
                        earned_coins = round(-2*amount)
                    elif calc == '6':
                        earned_coins = round(-2.3*amount)
                    elif calc == '7':
                        earned_coins = round(-2.8*amount)
                    elif calc == '8':
                        earned_coins = round(-3*amount)
                    elif calc == '9':
                        earned_coins = round(-4*amount)
                    
                    quote = 'gained'
                    if earned_coins < 0:
                        quote = 'lost'
                        
                    await update_bank(user,round(earned_coins))
                    
                    await bet_msg.delete()
                    bet_cr_embed = discord.Embed(
                        title = f"{user.name}, heres your bet",
                        description = f'You chose the number **`{bet_msg.content}`**\n\nThe dice rolled the number: **`{rand_dice}`** | You were `{calc}` numbers away from the dice 🎲\n*You {quote} `⌬ {earned_coins}` coins*',
                        color = discord.Colour.from_rgb(167,188,125)
                    )
                    await bet_embed.edit(embed=bet_cr_embed, mention_author = False)
                    
        except asyncio.TimeoutError:
            timeout_embed = discord.Embed(
                title = f"{user.name}, time's up 🎲",
                description = f"{user.mention}, you waited too long to choose a number\n*You lost `⌬ {round(amount/2)}` for not choosing a number in time*",
                color = discord.Color.from_rgb(219,69,65)
            )
            await bet_embed.delete()
            users[str(user.id)]['wallet'] -= round(amount/2)
            await ctx.reply(embed=timeout_embed, mention_author = True)
            with open('mainbank.json','w') as f:
                users = json.dump(users,f)
@dice.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        errors = ["wait a moment I'm currently hacking into your router","be patient meth doesn't cook that fast","i'm underpaid please wait for the cooldown"]
        errorem = discord.Embed(title=random.choice(errors),description="You're on a cooldown for this command, wait `{:.0f}` seconds to use it again".format(error.retry_after),color=discord.Colour.from_rgb(71,153,230))
        await ctx.reply(embed=errorem,mention_author=False,delete_after=4)  
    
@client.command(aliases=['steal'])
@commands.guild_only()
@commands.cooldown(1,30,commands.BucketType.user)
async def rob(ctx, member:discord.Member="SpecNone"):
    user = ctx.message.author
    await open_account(user)
    
    if member == "SpecNone":
        await ctx.reply(f'you need to specify a user to rob {fatkid}', mention_author=False)
        rob.reset_cooldown(ctx)
        return
    elif member == user:
        await ctx.reply(f"you can't rob yourself {skull}", mention_author=False)
        rob.reset_cooldown(ctx)
        return
        
    await open_account(member)
    bal = await update_bank(member)
        
    if bal[0] < 100:
        wdEmbed = discord.Embed(title=f"{user.name} rob someone else",description="it's not worth it, {} only has `⌬ {:,}` in their **wallet** {}".format(member.mention,bal[0],fatkid),color=discord.Colour.greyple())
        await ctx.reply(embed=wdEmbed, mention_author=False)
        return
        
    else:
        rate = ['Yes','No']
        rate_weights = random.choices(rate, weights=(69,39), k=2)
        sc_rates = random.choice(rate_weights)

        if sc_rates == 'No':
            f_rate = ['Yes','No']
            f_rate_weights = random.choices(f_rate, weights=(47,60), k=2)
            f_sc_rates = random.choice(f_rate_weights)

            if f_sc_rates == 'Yes':
                amount_lost = random.randint(20,150)
                wdEmbed = discord.Embed(title=f"{user.name} rob failed 🧨",description="You failed the rob and had to pay `⌬ {:,}` to {} {}".format(amount_lost,member.mention,skull),color=discord.Colour.from_rgb(222,68,62))
                await ctx.reply(embed=wdEmbed, mention_author=False)
                await update_bank(user,-1*amount_lost)
                await update_bank(member,amount_lost)

            elif f_sc_rates == 'No':
                    wdEmbed = discord.Embed(title=f"{user.name} rob failed, successfully 🚗",description=f"You failed the rob, but you did not get caught",color=discord.Colour.from_rgb(151,206,222))
                    await ctx.reply(embed=wdEmbed, mention_author=False)

        elif sc_rates == 'Yes':
            balis = bal[0]/1.5
            amount_won = random.randint(10,int(balis))

            wdEmbed = discord.Embed(title=f"{user.name} rob successful 🎉",description="You robbed `⌬ {:,}` from {} {}".format(amount_won, member.mention,printer))
            await ctx.reply(embed=wdEmbed, mention_author=False)
        
            await update_bank(user, amount_won)
            await update_bank(member,-1*amount_won)
@rob.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        rob.reset_cooldown(ctx)
    if isinstance(error, commands.CommandOnCooldown):
        errors = ["wait a moment I'm currently hacking into your router","be patient meth doesn't cook that fast","i'm underpaid please wait for the cooldown"]
        errorem = discord.Embed(title=random.choice(errors),description="You're on a cooldown for this command, wait `{:.0f}` seconds to use it again".format(error.retry_after),color=discord.Colour.from_rgb(71,153,230))
        await ctx.reply(embed=errorem,mention_author=False,delete_after=4)  
    
@client.command()
@commands.guild_only()
@commands.cooldown(1,696,commands.BucketType.user)
async def work(ctx, *, worked_as=''):
    user = ctx.message.author
    await open_account(user)
    users = await get_bank_data()
    
    as_a = ''
    if worked_as:
        as_a = f""" as a `{worked_as}`"""
    
    work_amt = random.randint(600,1600)
    users[str(user.id)]['wallet'] += work_amt
    em=discord.Embed(title=f"{user.name}, good work ✅",description="You worked long and hard{} and gained `⌬ {:,}`".format(as_a,work_amt,dollar),color=discord.Colour.from_rgb(178,250,143))
    await ctx.reply(embed=em,mention_author=False)
    with open('mainbank.json','w') as f:
        users = json.dump(users,f)
@work.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        errors = ["wait a moment I'm currently hacking into your router","be patient meth doesn't cook that fast","i'm underpaid please wait for the cooldown"]
        errorem = discord.Embed(title=random.choice(errors),description="You're on cooldown for this command, wait `{}` to use it again".format(time.strftime("%M minutes %S seconds",time.gmtime(error.retry_after))),color=discord.Colour.from_rgb(71,153,230))
        await ctx.reply(embed=errorem,mention_author=False,delete_after=7)

@client.command(aliases=['store'])
@commands.guild_only()
async def shop(ctx):
    user = ctx.message.author
    await open_account(user)
    users = await get_bank_data()

    global mainshop
    mainshop = [
    {"name": "Fruit", "price": 380, "description": "i love fruit"},
    {"name": "Phone", "price": 50, "description": "latest from china"},
    {"name": "Walter", "price": 1347, "description": "Walter"}
    ]
    
    em = discord.Embed(title="Shop [inflation may vary]",color = discord.Color.from_rgb(253,222,88))
    
    for item in list(mainshop):
        name = item['name']
        price = item['price']
        desc = item['description']
        
        em.add_field(name=name,value='`⌬{:,}` | {}'.format(price,desc),inline=False)
        
    await ctx.send(embed=em)
    
@client.command(aliases=['inv'])
@commands.guild_only()
async def inventory(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        inv = users[str(user.id)]["inv"]
    except:
        inv = []
    
    em = discord.Embed(title = "Inventory")
    for item in inv:
        name = item["item"]
        amount = item["amount"]
        
        if amount == 0:
            pass
        else:
            em.add_field(name = name, value = amount)    

    await ctx.send(embed = em) 
    
@client.command()
@commands.guild_only()
async def buy(ctx,*,args):
    await open_account(ctx.author)
    
    amount = 1
    integers = []
    item_letters = []
    for entry in list(args):
        try:
            integers.append(int(entry))
        except ValueError:
            item_letters.append(str(entry))
            
    if len(integers) != 0: 
        string_ints = [str(int) for int in integers]
        amount = int("".join(string_ints)) 
        
    item = str("".join(item_letters)).strip()
    res = await buy_this(ctx.author,item.strip(),amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have enough money in your wallet to buy {amount} {item}")
            return
        
    await ctx.send(f"You just bought {amount} {item}")
    
async def buy_this(user,item_name,amount):
    item_name = item_name.lower()

    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = round(price*amount)
    users = await get_bank_data()
    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]
    
    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["inv"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["inv"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["inv"].append(obj)
    except:
        obj = {"item":item_name , "amount" : amount}
        users[str(user.id)]["inv"] = [obj] 

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,round(cost*-1),"wallet")

    return [True,"Worked"]
    
@client.command()
@commands.guild_only()
async def sell(ctx,*,args):
    await open_account(ctx.author)
    
    amount = 1
    integers = []
    item_letters = []
    for entry in list(args):
        try:
            integers.append(int(entry))
        except ValueError:
            item_letters.append(str(entry))
            
    if len(integers) != 0: 
        string_ints = [str(int) for int in integers]
        amount = int("".join(string_ints)) 
        
    item = str("".join(item_letters)).strip()
    res = await sell_this(ctx.author,item.strip(),amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have {amount} {item} in your inv.")
            return
        if res[1]==3:
            await ctx.send(f"You don't have {item} in your inv.")
            return

    await ctx.send(f"You just sold {amount} {item}.")
    
async def sell_this(user,item_name,amount,price = None):
    item_name = item_name.lower()
    
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price==None:
                price = round(0.9* item["price"])
            break

    if name_ == None:
        return [False,1]

    cost = round(price*amount)
    users = await get_bank_data()
    bal = await update_bank(user)
    
    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["inv"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["inv"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            return [False,3]
    except:
        return [False,3]     

    with open("mainbank.json","w") as f:
        json.dump(users,f)
        
    await update_bank(user,round(cost),"wallet")

    return [True,"Worked"]

@client.command()
@commands.guild_only()
@commands.cooldown(1,30,commands.BucketType.user)
async def search(ctx):
    user = ctx.message.author
    await open_account(user)
    users = await get_bank_data()
    
    with open('places.json','r') as f:
        c_places = json.load(f)
        
    places = random.sample(list(c_places), 3)
    
    searchEm=discord.Embed( 
        title=f"{user.name}, search",description='🔻*type in chat a location you want to search*🔻\n`{}` | `{}` | `{}`'.format(places[0],places[1],places[2]),
        color=discord.Color.from_rgb(230,171,131)
    )
    searchEm.set_footer(text='30 seconds to choose❕')
    searchEm=await ctx.reply(embed=searchEm, mention_author=True)
    
    def check(m):
        return ctx.author == m.author
    try:
        msg = await ctx.bot.wait_for('message', timeout=35.0, check=check)
        
        if msg.content.capitalize() in list(places):
            await msg.delete()
            await searchEm.delete()
            msg = msg.content.capitalize()
            
            factor_weights = random.choice(random.choices(['live','die'],weights=(list(c_places[msg]['Weights'])), k=2))
            
            if factor_weights == 'die':
                coins_range = list(c_places[msg]['Coins'])
                coins_amount = random.randint(coins_range[0],coins_range[1])
                
                money_msg = '''*You died searching `{}`, you lost `{:,}` from your bank* 💸'''.format(msg.lower(),round(coins_amount*1.6))
                if users[str(user.id)]['wallet'] != 0:
                    money_msg = f'*You died searching `{msg.lower()}` and lost all your `money` in your wallet* 💸'
                
                die_embed = discord.Embed(
                    title=f'{user.name}, you died while searching',
                    description='''\n{} {}\n\n{}'''.format(''.join(list(c_places[msg]['Statement'][1])),skull,money_msg),
                    color = discord.Color.from_rgb(70,62,79)
                )
                await ctx.reply(embed=die_embed, mention_author = False)
                
                users = await get_bank_data() 
                
                if users[str(user.id)]['wallet'] != 0:
                    with_wallet_amt = users[str(user.id)]['wallet']
                    await update_bank(user,-1*with_wallet_amt)
                else:
                    with_bank_amt = users[str(user.id)]['bank']
                    await update_bank(user,round(coins_amount*1.6)*-1,'bank')

            elif factor_weights == 'live':
                coins_range = list(c_places[msg]['Coins'])
                coins_amount = random.randint(coins_range[0],coins_range[1])
                
                live_embed = discord.Embed(
                    title=f'{user.name}, search successful  🎋',
                    description='''You searched `{}` and found `⌬ {:,}`\n\n*{}*'''.format(msg.lower(),coins_amount,''.join(''.join(list(c_places[msg]['Statement'][0])))),
                    color=discord.Color.from_rgb(203,230,168)
                )
                await ctx.reply(embed=live_embed, mention_author = False)
            
                await update_bank(ctx.author,coins_amount)
                
        elif msg.content.capitalize() not in list(places):
            await searchEm.delete()
            non_embed = discord.Embed(
                title = f"{user.name}, did you even read the options",
                description = f"{user.mention}, what you chose was not in the options for locations {skull}",
                color = discord.Color.from_rgb(232,67,60)
            )
            await ctx.reply(embed=non_embed, mention_author = True)
            
    except asyncio.TimeoutError:
        await searchEm.delete()
        timeout_embed = discord.Embed(
            title = f"{user.name}, time's up",
            description = f"{user.mention}, you waited too long to search for a location {skull}",
            color = discord.Color.from_rgb(232,67,60)
        )
        await ctx.reply(embed=timeout_embed, mention_author = True)
@search.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        errors = ["wait a moment I'm currently hacking into your router","be patient meth doesn't cook that fast","i'm underpaid please wait for the cooldown"]
        errorem = discord.Embed(title=random.choice(errors),description="You're on a cooldown for this command, wait `{:.0f}` seconds to use it again".format(error.retry_after),color=discord.Colour.from_rgb(71,153,230))
        await ctx.reply(embed=errorem,mention_author=False,delete_after=4)  
        
@client.command(aliases=['with'])
@commands.guild_only()
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
    emsu.add_field(name="Current bank balance",value="`⌬ {:,} / ⌬ {:,}`".format(users[str(user.id)]["bank"],users[str(user.id)]["limit_bank"]))
    await ctx.reply(embed=emsu,mention_author=False)
    
@client.command(aliases=['dep'])
@commands.guild_only()
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
        
      if wallet_amt+bal[1] > users[str(user.id)]["limit_bank"]:
            bala = bal[1]
            max_amount = users[str(user.id)]["limit_bank"]
            
            subtract_amount = bala - max_amount
            amount_subtractive = wallet_amt - abs(subtract_amount)
            final_amount = wallet_amt - abs(amount_subtractive)
            
            await update_bank(ctx.author,-1*final_amount)
            await update_bank(ctx.author,final_amount,"bank")
            
            emsu = discord.Embed(title="Deposit",description="You deposited `⌬ {:,}`".format(final_amount),color=discord.Colour.from_rgb(237,240,240))
            
      else:
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
        
        if amount+bal[1] > users[str(user.id)]["limit_bank"]:
            bala = bal[1]
            max_amount = users[str(user.id)]["limit_bank"]
            
            subtract_amount = bala - max_amount
            amount_subtractive = amount - abs(subtract_amount)
            final_amount = amount - abs(amount_subtractive)
            
            await update_bank(ctx.author,-1*final_amount)
            await update_bank(ctx.author,final_amount,"bank")
            
            emsu = discord.Embed(title="Deposit",description="You deposited `⌬ {:,}`".format(final_amount),color=discord.Colour.from_rgb(237,240,240))
            
        else:
            await update_bank(ctx.author,-1*amount)
            await update_bank(ctx.author,amount,"bank")
            
            emsu = discord.Embed(title="Deposit",description="You deposited `⌬ {:,}`".format(amount),color=discord.Colour.from_rgb(237,240,240))
      
    users = await get_bank_data()
    emsu.add_field(name="Current wallet balance",value="`⌬ {:,}`".format(users[str(user.id)]["wallet"]))
    emsu.add_field(name="Current bank balance",value="`⌬ {:,} / ⌬ {:,}`".format(users[str(user.id)]["bank"],users[str(user.id)]["limit_bank"]))
    await ctx.reply(embed=emsu,mention_author=False)
  
@client.command(aliases=['give','transfer'])
@commands.guild_only()
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
    
    amount = int(amount)
    bal = await update_bank(ctx.author)
    if amount>bal[1]:
      await ctx.reply("either you aren't rich enough to give `⌬ {:,}`, or you forgot to deposit it in your bank before giving it {}".format(amount,fatkid),mention_author=False) 
      return
    if amount<=0:
      await ctx.reply(f'thats impossible lol, send an amount of money greater than 0',mention_author=False) 
      return
  
    recipient_bank_limit = users[str(member.id)].get("limit_bank", float("inf"))
    if amount + users[str(member.id)]["bank"] > recipient_bank_limit:
        await ctx.reply("You can't send `⌬ {:,}` to {} because it would exceed their bank limit of `⌬ {:,}`".format(amount,member.mention, recipient_bank_limit), mention_author=False)
        return
  
    # if amount + users[str(member.id)]["bank"] > users[str(member.id)]["limit_bank"][0]:
    if amount + users[str(member.id)]["bank"] > users[str(member.id)]["limit_bank"]:
            bala = users[str(member.id)]["bank"]
            max_amount = users[str(member.id)]["limit_bank"][0]
            
            subtract_amount = bala - max_amount
            amount_subtractive = amount - abs(subtract_amount)
            final_amount = amount - abs(amount_subtractive)
            
            await update_bank(ctx.author,-1*final_amount,"bank")
            await update_bank(member,final_amount,"bank")
            
            users = await get_bank_data()
            sendem = discord.Embed(title="Money sent",description="You sent `⌬ {:,}` to {} {}".format(final_amount,member.mention,moni),color=discord.Colour.from_rgb(188,206,219))
            sendem.set_footer(text='put those ⌬ to good use {}, or not, i dont care'.format(member.name))

    else:
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
        errorem = discord.Embed(title=random.choice(errors),description="You're on a cooldown for this command, wait `{:.0f}` seconds to use it again".format(error.retry_after),color=discord.Colour.from_rgb(71,153,230))
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
    
@client.command(aliases=['credit'])
async def credits(ctx):
    creditEm= discord.Embed(
        title='Credits 📜',
        description='''*Thank you to all the people who have helped me on this bot and made it possible 🌹 ⠀⠀⠀- <@680154732567855259>*
        ━━━━━━━━━━━━
        
        `Bot owner & Developer` : <@680154732567855259>
        `Project Supervisor` : <@520439192925241355>
        
        `Helpers with locations on the search command` :
        > <@338008145626529793>
        > <@520439192925241355>
        > <@528394152845639690>
        > <@760179479506321408>
        
        `Cooldown quote maker` : <@704508007429439559>
        ''',
        color=discord.Color.orange()
    )
    await ctx.reply(embed=creditEm, mention_author=False)
    
@client.command()
@commands.guild_only()
@commands.has_role(831032289411465256)
async def crash(ctx):
    user = ctx.author
    crashEm= discord.Embed(
        title=f'‼ WARNING ‼',
        description=f"{user.name}, are you sure you want to crash the economy? This will clear **everyone's** balance, this is **irreversable** ⚠\n\n[ `Yes` / `No` ]",
        color=discord.Color.from_rgb(219,40,40)
    )
    crashEm.set_footer(text='This will expire in 40 SECONDS')
    crashEm= await ctx.reply(embed=crashEm,mention_author=True)
    
    responses_yes = ['yes','Yes','Y','y','yeah']
    responses_no = ['no','No','N','n','nah']
    
    def check(m):
        return ctx.author == m.author
    try:
        msg = await ctx.bot.wait_for('message', timeout=40.0, check=check)
        
        if msg.content in responses_yes:
            await msg.delete()
            await crashEm.delete()
            
            crashEm= discord.Embed(
                title=f'Economy has been crashed 📉',
                description=f"{user.mention}, you have crashed the economy.\nEveryone is back to their starter balance",
                color=discord.Color.from_rgb(211,230,151)
            )
            crashEm= await ctx.reply(embed=crashEm,mention_author=False)
            
            open('mainbank.json', 'w').close()
            
            with open('mainbank.json', 'w') as f:
                f.write('{}')

        elif msg.content in responses_no:
            await msg.delete()
            await crashEm.delete()
            
            crashEm= discord.Embed(
                title=f'Economy crash was cancelled 🚧',
                description=f"{user.mention} you have cancelled crashing the economy.\nThe economy lives to see another day",
                color=discord.Color.from_rgb(211,230,151)
            )
            crashEm= await ctx.reply(embed=crashEm,mention_author=False)
            
        elif msg.content not in responses_yes or responses_no:
            await msg.delete()            
            await crashEm.delete()
            non_embed = discord.Embed(
                title = f"{user.name}, your answer is not in the options ❔",
                description = f"{user.name}, what you chose was not in the options for crashing the economy {fatkid}",
                color = discord.Color.from_rgb(232,67,60)
            )
            await ctx.reply(embed=non_embed, mention_author = True)
            
    except asyncio.TimeoutError:
        await msg.delete()        
        await crashEm.delete()
        timeout_embed = discord.Embed(
            title = f"{user.name}, time ran out ⏰",
            description = f"The economy lives to see another day 📈",
            color = discord.Color.from_rgb(232,67,60)
        )
        await ctx.reply(embed=timeout_embed, mention_author = True)
        
@client.command()
@commands.guild_only()
@commands.has_role(831032289411465256)
async def change(ctx,member:discord.Member,amount:str,selection:str='wallet'):
    user = ctx.author
    await open_account(ctx.author)
    await open_account(member)
    users = await get_bank_data()
    
    parsed_amount = amount
    if int(parsed_amount) >= 0:
        
        if '+' in amount:
            parsed_amount = int(amount.replace('+',''))
            
        if selection == "bank" or 'Bank':
            await update_bank(member,int(parsed_amount),selection)
            
        elif selection == 'wallet' or "wallet":
            await update_bank(member,int(parsed_amount),selection)
            
        users = await get_bank_data()
            
        non_embed = discord.Embed(
            title = f"{user.name}, you changed a balance 📈",
            description = "You added `⌬ {:,}` to {}'s **{}** {}".format(int(parsed_amount),member.mention, selection, printer),
            color = discord.Color.from_rgb(211,230,151)
        )
        non_embed.add_field(name=f"{member.name}'s wallet",value="`⌬ {:,}`".format(users[str(member.id)]['wallet']))
        non_embed.add_field(name=f"{member.name}'s bank",value="`⌬ {:,}`".format(users[str(member.id)]['bank']))
        await ctx.reply(embed=non_embed, mention_author = False)
        
    elif int(parsed_amount) < 0:
        
        if '-' in amount:
            parsed_amount = int(amount.replace('-',''))
        
        if selection == "bank" or 'Bank':
            await update_bank_negative(member,int(parsed_amount),selection)
            
        elif selection == 'wallet' or "wallet":
            await update_bank_negative(member,int(parsed_amount),selection)
            
        users = await get_bank_data()
            
        non_embed = discord.Embed(
            title = f"{user.name}, you changed a balance 📉",
            description = "You **removed** `⌬ {:,}` from {}'s **{}** {}".format(int(parsed_amount), member.mention,selection, '💸'),
            color = discord.Color.from_rgb(211,230,151)
        )
        non_embed.add_field(name=f"{member.name}'s wallet",value="`⌬ {:,}`".format(users[str(member.id)]['wallet']))
        non_embed.add_field(name=f"{member.name}'s bank",value="`⌬ {:,}`".format(users[str(member.id)]['bank']))
        await ctx.reply(embed=non_embed, mention_author = False)

#  -     -                
        
async def open_account(user):
    users = await get_bank_data()
        
    if str(user.id) in users:
            return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]['wallet'] = 6
        users[str(user.id)]['bank'] = 52
        users[str(user.id)]['limit_bank'] = 30000
            
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

async def update_bank_negative (user,change = 0,mode = 'wallet'):
    users = await get_bank_data() 

    users[str(user.id)][mode] -= change 

    with open("mainbank.json","w") as f:
      json.dump(users,f) 
    bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
    return bal

async def get_bank_data():
    with open('mainbank.json','r') as f:
        users = json.load(f)
    return users

client.run(TOKEN['token'])
