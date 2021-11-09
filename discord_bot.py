import discord
from discord import client
from discord import message
from discord.ext import commands
import urllib.request, json
import json
from discord.webhook import AsyncWebhookAdapter
from types import SimpleNamespace
import time
import csv


import requests
import re
import random

# ------ #TODO# ------
# 1# Fix winning message
# 2# SAVE SCORE (LOOP AS .CSV AND SAVE AFTER WIN)
#    Play music when start a game...
#    
# 3# more games / categories 

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='.',intents=intents)
client.remove_command('help')

#***********************************************#
# REMOVE WHEN DONE 
# REMOVE WHEN DONE 
# REMOVE WHEN DONE 
# REMOVE WHEN DONE 
# REMOVE WHEN DONE 
# REMOVE WHEN DONE 

@client.command()
async def sex(ctx):
    await ctx.send("Im gonna ass fuck you!")

@client.command()
async def jew(ctx):
    embed = discord.Embed(
        color=discord.Color.red()
    )
    embed.set_author(name='HEATING SHOWERS')
    embed.add_field(name="These are gonna be toasty", value='Yumm!', inline="False")
    
    message = await ctx.send(embed=embed)

    time.sleep(2)

    await message.delete()

@client.command()
async def mat(ctx):
    await ctx.send("Mat fag")

@client.command()
async def sus(ctx):
    await ctx.send("Sacha")

@client.command()
async def tom(ctx):
    await ctx.send("I failed math three times!!")


@client.command(aliases=['beaner', 'spic'])
async def carlos(ctx):
    massge = await ctx.send("nigger")
    time.sleep(2)
    ctx.message.delete()


@client.command()
async def kys(ctx):
    await ctx.send("kys @"+str(ctx.author.name))

    #mateus
@client.command()
async def antivax(ctx):
    await ctx.send("Mateus lul: GoVerNment is GonNA CoNtRoL mE")



# REMOVE WHEN DONE 
# REMOVE WHEN DONE 
# REMOVE WHEN DONE 
# REMOVE WHEN DONE 
# REMOVE WHEN DONE 
# REMOVE WHEN DONE
#******************************************************************#

@client.event
async def on_ready():
    print("Bot is ready")



@client.command()
async def getmember(ctx):
    username = ctx.message.author.name
    if(str(username) == "TheMemer27"):
        member_list = ''
        for member in ctx.guild.members:
            member_list += member.name
            print(member.name)
            await ctx.send(member.name)

    else:
        await ctx.send("Youre not admin")


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
        i = 5
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
    user_list = []
    if str(user) not in user_list:
        print("=========== ADDED TO LIST ==============")
        user_list += [user]
        print(user_list)
    else:
        print("=--=--=-=-=- DUPLICATED =-=-=-=-=")
    
    reactions = reaction.message.reactions
    # DO WHAT YOU WANT HERE 
    if(str(user) != "BeanerBot#0361"):

        print(str(user) +"\t "+ str(reaction))

        if(str(reaction) == "<:pepe:829529597078536212>"):
            if (user_list[0] == user):

                print("=========== WINNER MESSAGGE ===============")

                #await reaction.message.delete()
                
                embed = discord.Embed(
                    color=discord.Color.green()
                    )  
                embed.title = 'Winner'
                embed.add_field(name=(str(user)), value="Has won 50 Social Credits!", inline="False")

                await reaction.message.edit(embed=embed)
        else:
            print("=========== GAME END ===============")

            #await reaction.message.delete()
            
            embed = discord.Embed(
                color=discord.Color.red()
                )  
            embed.title = 'Looser'
            embed.add_field(name=(str(user)), value="Hold this: L", inline="False")

            await reaction.message.edit(embed=embed)
           # new(user)


def new(user):
    
    print(user)
    @client.event
    async def newWinner(ctx):
        # DO WHAT YOU WANT HERE 
        if(str(user) != "BeanerBot#0361"):

            embed = discord.Embed(
                color=discord.Color.green()
                )  
            embed.title = 'Winner'
            embed.add_field(name=(str(user)), value="Has won 50 points!", inline="False")

            print("_-__-__-__-__-__- SENDING MESSAGE -__---_--__-_--__-")
            # Sending message??
            message = await ctx.send(embed=embed)
            await ctx.send(embed=embed)
        

            



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