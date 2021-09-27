import discord
from discord.ext import commands #.ext means extension presumably
import Secret_Stuff
import random
import sentiment_analysis
client = commands.Bot(command_prefix=".")

@client.event #function decorator => basically says the next line is going to be a event function
async def on_ready():
    print('Bot is ready!!')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases = ['8ball'])
async def _8ball(ctx, *, question): #* allows to take multiple arguments
    responses = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.",
                 "Very doubtful.", "Without a doubt.",
                 "Yes.", "Yes – definitely.", "You may rely on it."]
    await ctx.send(f'Question: {question}\n Answer: {random.choice(responses)}')

@client.event
async def on_message(message):
    name = 'Cyber_Safer'
    tag = "<@!890457950265688074>"
    print(f'{message.author} has sent the message: {message.content}')
    if sentiment_analysis.analyze(message.content) == 0:
        mention = message.author.mention
        if name in message.content or tag in message.content:
            response = f"{mention}, don't talk about your dad like that!"
        else:
            response = f"hey {mention}, maybe chill a bit"
            print(response)
        await message.channel.send(response)




client.run(Secret_Stuff.token)
