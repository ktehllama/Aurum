# Aurum [v0.10.3]
## _Monetizing the Benzene Ring ASCII character since 2022_

Aurum is a high performance, minigame filled,

- Python 3 powered Discord economy bot.
- Lots of commands, fun for the whole server
- 🔥 Leaderboard for the tryhards 🔥

## Features

- JSON stored balances so you never lose your progress
- Automated account creation
- In depth help commands
- Easy to start using
- 30+ commands in the full version (v.1.3.0)
- Various locations for the search command

Containing helper functions and cogs for all different types of integrations and high
responsiveness assured, Aurum's commands are full with features. Complete with a
pagination system for easy access, the help command is in depth and even allows
you to see help of a specific command. You can rob people, lose everything in the slots
or win big and then stash everything in your personal bank (that has a limit unless you buy more in-game),
the possibilities are really endless. For the admins, you can reset the economy completely 
using the `crash` command, (just remember to change the `has_role` id checker to your admin roles' id) 
or with your omnipotent god powers, reach into anyone's wallet or bank and add or substract any amountof money. 
Aurum's flagship command though is the `search` command where you have the choice to search 3 different
locations for various sums of money, or lose everything. You can even add your own locations, probabilities
and money! My favorite location is the `shiny green portal` btw.

> Note:
In the updated version (v.1.3.0) there are more commands such as a stock market exchange
and many more locations along with more items to buy in the shop, I might release the
new version, or it just might escape from my hard drive, depending on the reviews
this gets.

## Tech
Aurum uses a number of projects to work properly:

- [Python](https://www.python.org/downloads/)
- [Discord.py](https://discordpy.readthedocs.io/)
- JSON

And of course Aurum itself is open source with a [public repository](https://github.com/ktehllama/Aurum/)
on GitHub.

## Installation
Aurum requires [Python](https://www.python.org/downloads/) 3.10+ to run.

Make a Discord bot in the [Discord Developer Portal](https://discord.com/developers/docs/intro),
get it's token and replace it with the constant `TOKEN` in `core.py` to run. Add your own
prefix or use the one already in place.
```python
    client = commands.Bot(command_prefix = ['.'])
    TOKEN = "BOT-TOKEN-HERE"
```
For the emojis to work, your bot or you will need to be added to the server containing them, 
please ask to be added or remove all emojis variables from the code for the bot to work correctly.

You can also change the Benzene Ring ASCII (`⌬`) and replace it for something else for your currency, but
you will have to replace each one individually as in this version I have not implimented a centralized
variable for currency change.

Make sure to correctly link the `mainbank.json` and `places.json` file paths correctly in the helper functions 
(`open_account`,`update_bank`,`update_bank_negative`,`get_bank_data`; for `mainbank.json`
`search` command for `places.json`).

Remember to use `pip install` in the terminal to install all dependencies/packages

## Dependencies
Aurum currently uses the following packages.
If they have an ❌next to them then they require
installation via `pip`:
| Package | Included with python? |
| ---- | ---- |
| [Discord.py](https://discordpy.readthedocs.io/) | ❌
| asyncio | ✅
| DiscordUtils | ❌
| json | ✅
| random | ✅
| time | ✅
| datetime | ✅

## Afterword
This bot was a culmination of multiple that came before, he is maybe the 5th generation economy bot
I have created and its predecessor Aurum v1.3.0 is not yet released to this repository; it's much more
complete and with way more features that I'm very proud of, no matter how many hours I had to
debug in [VsCode](https://code.visualstudio.com/), I always found it nice that people could later enjoy
my creation on other Discord servers. I invite you to take inspiration from this bot and it's commands,
as making an economy bot isn't that hard, its coming up with new commands and thingamajigs that really count.
Aurum has taught me alot in the coding, and even more in how Discord Bots work. Hopefully you can enjoy
what it has to offer as much as I did, or just copy-paste some code from him that you needed to finish a 
bot of your own, we've all done it at some point :)

-ktehllama

## License
CC0-1.0
_For real_
