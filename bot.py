import discord
from discord.ext import commands #.ext means extension presumably
import Secret_Stuff

client = commands.Bot(command_prefix=".")

@client.event #function decorator => basically says the next line is going to be a event function
async def on_ready():
    print('Bot is ready!!')

client.run(Secret_Stuff.token)
