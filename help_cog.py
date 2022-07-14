from attr import field
import discord
from discord.ext import commands
import DiscordUtils

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
     
    @commands.command()
    async def help(self, ctx, cmd=None):
        if cmd == None:
            help1 = discord.Embed(title='Help (Economy  🏦)',description="> **balance**\n━━━━━━━━\n> **beg**\n━━━━━━━━\n> **search**\n━━━━━━━━\n> **deposit**\n━━━━━━━━\n> **dice**\n━━━━━━━━\n> **leaderboard**\n━━━━━━━━\n> **rob**\n━━━━━━━━\n> **send**\n━━━━━━━━\n> **slots**\n━━━━━━━━\n> **withdraw**\n━━━━━━━━\n> **work**",color=ctx.author.color).set_footer(text='Use .help [command name] to see help for a specific command ❕')
            help2 = discord.Embed(title='Help (Random 🦖)',description="> **fruit**\n━━━━━━━━\n> **credit**",color=ctx.author.color).set_footer(text='Use .help [command name] to see help for a specific command ❕')
            
            paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx)
            
            paginator.add_reaction('⏮️', "first")
            paginator.add_reaction('⏪', "back")   
            paginator.add_reaction('⏩', "next")
            paginator.add_reaction('⏭️', "last")
            embeds = [help1, help2]
            await paginator.run(embeds)
        else:
            if cmd == 'balance':
                helpEm = discord.Embed(
                    title='Command: balance',
                    description='''> See your account balance or someone elses.''',
                    color=discord.Colour.from_rgb(131,199,222)
                )
                helpEm.add_field(name='Syntax',value="`.balance [@user (optional)]`", inline=False)
                helpEm.add_field(name='Alternatives',value="`bal`", inline=False)
                helpEm.add_field(name='Cooldown time',value="`None`", inline=False)
                await ctx.reply(embed=helpEm, mention_author=False)
                
            elif cmd == 'beg':
                helpEm = discord.Embed(
                    title='Command: beg',
                    description='''> Beg for money.
                    
                    You have a chance of not getting money''',
                    color=discord.Colour.from_rgb(131,199,222)
                )
                helpEm.add_field(name='Syntax',value="`.beg`", inline=False)
                helpEm.add_field(name='Cooldown time',value="`15 seconds`", inline=False)
                await ctx.reply(embed=helpEm, mention_author=False)
                
            elif cmd == 'deposit':
                helpEm = discord.Embed(
                    title='Command: deposit',
                    description='''> Deposit money from your wallet to your bank.
                    
                    You can't deposit if there's nothing in your wallet or if you deposit an amount you don't have or an amount that is 0 or below 0''',
                    color=discord.Colour.from_rgb(131,199,222)
                )
                helpEm.add_field(name='Syntax',value="`.dep [amount]`", inline=False)
                helpEm.add_field(name='Alternatives',value="`dep`", inline=False)
                helpEm.add_field(name='Cooldown time',value="`None`", inline=False)
                await ctx.reply(embed=helpEm, mention_author=False)
                
            elif cmd == 'dice':
                helpEm = discord.Embed(
                    title='Command: dice',
                    description='''> Gamble on a dice.
                    
                    You will be prompted to choose a number 1 through 10, and the bot will choose a number itself, if you choose the exact number it chose, you get the money you bet times 5.
                    Else, you will get less money the further away you were from the number''',
                    color=discord.Colour.from_rgb(131,199,222)
                )
                helpEm.add_field(name='Syntax',value="`.dice [bet amount]`", inline=False)
                helpEm.add_field(name='Cooldown time',value="`50 seconds`", inline=False)
                await ctx.reply(embed=helpEm, mention_author=False)
                
            elif cmd == 'leaderboard':
                helpEm = discord.Embed(
                    title='Command: leaderboard',
                    description='''> See the top 5 richest users of the server.
                    
                    It calculates your richness by adding your wallet and bank amount.''',
                    color=discord.Colour.from_rgb(131,199,222)
                )
                helpEm.add_field(name='Syntax',value="`.leaderboard`", inline=False)
                helpEm.add_field(name='Alternatives',value="`lb`", inline=False)
                helpEm.add_field(name='Cooldown time',value="`None`", inline=False)
                await ctx.reply(embed=helpEm, mention_author=False)
                
            elif cmd == 'rob':
                helpEm = discord.Embed(
                    title='Command: rob',
                    description='''> Rob other users of their money.
                    
                    The rob command robs users from their wallet, if they don't have anything in their wallet then you can't rob them.
                    You can't rob someone who has less than `⌬ 100` in their wallet. There is a chance you can fail the robbery, in that situation, you can either fail the robbery and not get caught, or get caught and have to pay the person you were robbing money.
                    ''',
                    color=discord.Colour.from_rgb(131,199,222)
                )
                helpEm.add_field(name='Syntax',value="`.rob [@user]`", inline=False)
                helpEm.add_field(name='Alternatives',value="`steal`", inline=False)
                helpEm.add_field(name='Cooldown time',value="`20 seconds`", inline=False)
                await ctx.reply(embed=helpEm, mention_author=False)
        
            elif cmd == 'send':
                helpEm = discord.Embed(
                    title='Command: send',
                    description='''> Send money to another user.
                    
                    You must deposit the money you want to send in your bank first, since sending money sends money from **your bank** to the **other person's bank**
                    You must send an amount greater than 0 and you cannot send yourself money.''',
                    color=discord.Colour.from_rgb(131,199,222)
                )
                helpEm.add_field(name='Syntax',value="`.send [@user] [amount]`", inline=False)
                helpEm.add_field(name='Alternatives',value="`give`,`transfer`", inline=False)
                helpEm.add_field(name='Cooldown time',value="`10 seconds every 5 commands`", inline=False)
                await ctx.reply(embed=helpEm, mention_author=False)
                
            elif cmd == 'slots':
                helpEm = discord.Embed(
                    title='Command: slots',
                    description='''> Play some slots!
                    
                    In slots you have to bet an amount of money of 2 or above. There are fruits and a bomb, more fruits you match of the same kind more money.
                    If you get 3 of a kind of the same fuityou get a significant amount of money. 
                    
                    If you get 2 bombs, you lose money, match 3 bombs and you lose a lot of money.
                    
                    If you don't get any matches you just lose the amount of money you bet''',
                    color=discord.Colour.from_rgb(131,199,222)
                )
                helpEm.add_field(name='Syntax',value="`.slots [bet amount]`", inline=False)
                helpEm.add_field(name='Alternatives',value="`slot`", inline=False)
                helpEm.add_field(name='Cooldown time',value="`25 seconds`", inline=False)
                await ctx.reply(embed=helpEm, mention_author=False)
                
            elif cmd == 'withdraw':
                helpEm = discord.Embed(
                    title='Command: withdraw',
                    description='''> Withdraw money from your bank to your wallet.
                    
                    You can't withdraw if there's nothing in your bank or if you withdraw an amount you don't have or an amount that is 0 or below 0''',
                    color=discord.Colour.from_rgb(131,199,222)
                )
                helpEm.add_field(name='Syntax',value="`.withdraw [amount]`", inline=False)
                helpEm.add_field(name='Alternatives',value="`with`", inline=False)
                helpEm.add_field(name='Cooldown time',value="`None`", inline=False)
                await ctx.reply(embed=helpEm, mention_author=False)
                
            elif cmd == 'work':
                helpEm = discord.Embed(
                    title='Command: work',
                    description='''> Work for money.
                    
                    You can type text after work such as "among us" and it will say:
                    *You worked long and hard as an `among us` and won money*
                    
                    Pro tip: Don't type anything against the rules.''',
                    color=discord.Colour.from_rgb(131,199,222)
                )
                helpEm.add_field(name='Syntax',value="`.work [text (optional)]`", inline=False)
                helpEm.add_field(name='Cooldown time',value="`1 hour 30 minutes`", inline=False)
                await ctx.reply(embed=helpEm, mention_author=False)
                
            elif cmd == 'fruit':
                helpEm = discord.Embed(
                    title='Command: fruit',
                    description='''> Sends a random fruit.''',
                    color=discord.Colour.from_rgb(131,199,222)
                )
                helpEm.add_field(name='Syntax',value="`.fruit`", inline=False)
                helpEm.add_field(name='Cooldown time',value="`None`", inline=False)
                await ctx.reply(embed=helpEm, mention_author=False)
                
            elif cmd == 'credits':
                helpEm = discord.Embed(
                    title='Command: credits',
                    description='''> Shows the credits for the bot.''',
                    color=discord.Colour.from_rgb(131,199,222)
                )
                helpEm.add_field(name='Syntax',value="`.credits`", inline=False)
                helpEm.add_field(name='Alternatives',value="`credit`", inline=False)
                await ctx.reply(embed=helpEm, mention_author=False)
                
            elif cmd == 'search':
                helpEm = discord.Embed(
                    title='Command: search',
                    description='''> Search for money in various locations.
                    
                    You will be prompted with `3` locations, of which you have to choose one and type it below in chat.
                    You have a chance of living and getting money, or dying, and losing **everything** in your **wallet**''',
                    color=discord.Colour.from_rgb(131,199,222)
                )
                helpEm.add_field(name='Syntax',value="`.search`", inline=False)
                helpEm.add_field(name='Cooldown time',value="`20 seconds`", inline=False)
                await ctx.reply(embed=helpEm, mention_author=False)