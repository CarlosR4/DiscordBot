import discord
from discord import client
from discord import message
from discord.ext import commands
import urllib.request, json
import json
from discord.webhook import AsyncWebhookAdapter
from types import SimpleNamespace
import time

import requests
import re
import random

# ------ #TODO# ------
# 1# send winning message 
# 2# SAVE SCORE (LOOP AS .CSV AND SAVE AFTER WIN)
# 3# more games / categories 

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='.',intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def getmember(ctx):
    member_list = ''
    for member in ctx.guild.members:
        member_list += member.name
        print(member.name)


@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

@client.command()
async def ping(ctx):
    await ctx.send(f"pong: {round(client.latency*1000)}ms" )


@client.command()
async def hi(ctx):
    await ctx.send("Hello I am BeanerBot.")
    

@client.command()
async def help(ctx):
    embed = discord.Embed(
        color=discord.Color.orange()
    )
    embed.set_author(name='Help')
    embed.add_field(name=".trivia", value='Starts a quick game of Trivia', inline="False")
    
    await ctx.send(embed=embed)

@client.command()
async def trivia(ctx):
    #url = 'https://opentdb.com/api.php?amount=1'
    url = 'https://opentdb.com/api.php?amount=1&category=18&difficulty=medium&type=multiple'
    req = urllib.request.Request(url)

    ##parsing response
    r = urllib.request.urlopen(req).read()
    cont = json.loads(r.decode('utf-8'), object_hook=lambda d: SimpleNamespace(**d))
    counter = 0
    print(cont)
    ##parcing json
    for question in cont.results:
        counter += 1
        print("Category:" + question.category +"\n Question:"+question.question+ "\nAwnsers:"+ str(question.incorrect_answers))
        print("----")

        embed = discord.Embed(
        color=discord.Color.green()
        )   
        embed.title= 'Trivia!'
        embed.add_field(name="Category", value=(question.category), inline="False")
        embed.add_field(name="Type", value=(question.type), inline="False")
        embed.add_field(name="Difficulty", value=(question.difficulty), inline="False")
        message = await ctx.send(embed=embed)
        i = 1
        while i > 0:
            print(i)

            time.sleep(1)

            embed.title= ('Trivia! '+f"{i}s")
            
            await message.edit(embed=embed)
            i -= 1


        embed.title= ('Trivia! Starting...')

        await message.edit(embed=embed)

        await message.delete()

        emoji = discord.utils.get(ctx.guild.emojis, name="pepe")

        embed2 = discord.Embed(
        color=discord.Color.green()
        )  

        embed2.title= 'Trivia!'
        embed2.title= question.question
        embed2.add_field(name=("🅰 : "+str(question.incorrect_answers[0])), value="_______", inline="False")
        embed2.add_field(name=("🅱️ : "+str(question.incorrect_answers[1])), value="_______", inline="False")
        embed2.add_field(name=("© : "+str(question.incorrect_answers[2])), value="_______", inline="False")
        embed2.add_field(name=("Pepe : "+str(question.correct_answer)), value="_______", inline="False")

        ##embed2.add_field(name="Asnwers", value=(question.incorrect_answers), inline="False")

        message2 = await ctx.send(embed=embed2)
        
        await message2.add_reaction("🅰" )
        await message2.add_reaction("🅱️")
        await message2.add_reaction("©")
        await message2.add_reaction(str(emoji))

        time.sleep(3)
    
@client.event
async def on_reaction_add(reaction, user):
    reactions = reaction.message.reactions
    # DO WHAT YOU WANT HERE 
    if(str(user) != "BeanerBot#0361"):
        print(str(user) +"\t "+ str(reaction))
        if(str(reaction) == "<:pepe:829529597078536212>"):
            print("=========== NEW WINNER ===============")
            await reaction.message.delete()
            embed = discord.Embed(
                color=discord.Color.green()
                )  
            embed.title = 'Winner'
            embed.add_field(name=(str(user)), value="Has won 50 points!", inline="False")

            newWinner(user)

@client.event
async def newWinner(user,ctx):
    # DO WHAT YOU WANT HERE 
    if(str(user) != "BeanerBot#0361"):
        print("=========== NEW WINNER ===============")

        embed = discord.Embed(
            color=discord.Color.green()
             )  
        embed.title = 'Winner'
        embed.add_field(name=(str(user)), value="Has won 50 points!", inline="False")

        message = await ctx.send(embed=embed)
            

            



    #Working code (more complicated)
    '''
    r = requests.get(url='https://opentdb.com/api.php?amount=2')
    print(r.json())
    #data_ = json.loads(str(r))

    await ctx.send("Received Trivia Questions...")
    await ctx.send(r.json())
    
    with urllib.request.urlopen("") as url:
        data = json.loads(url.read().decode())
        data_dict = json.loads(data)

        print(data)
        print(data_dict['question'])
        await ctx.send("Received Trivia Questions...")
    '''
    



client.run('ODE2MTc4MDAwMTY3OTYwNjE2.YD3K_w.0jaZ7zEcU3aBkq-UU5j0t2MxXZ4')