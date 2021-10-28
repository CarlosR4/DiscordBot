import discord
from discord import client
from discord.ext import commands
import urllib.request, json
import json


client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print("Bot is ready")


@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

@client.command()
async def ping(ctx):
    await ctx.send(f"pong: {round(client.latency*1000)}/ms" )


@client.command()
async def hi(ctx):
    await ctx.send("Hello I am BeanerBot.")
    
@client.command()
async def trivia(ctx):
    with urllib.request.urlopen("https://opentdb.com/api.php?amount=10") as url:
        data = json.loads(url.read().decode())
        data_dict = json.loads(data)

        print(data)
        print(data_dict['question'])
        await ctx.send("Received Trivia Questions...")
    



client.run('ODE2MTc4MDAwMTY3OTYwNjE2.YD3K_w.0jaZ7zEcU3aBkq-UU5j0t2MxXZ4')