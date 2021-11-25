from logging import error
import discord
from discord import client
from discord import message
from discord.ext import commands
import urllib.request, json
import json
from discord.utils import async_all
from discord.webhook import AsyncWebhookAdapter
from types import SimpleNamespace
import time
import csv
import os
from discord import FFmpegPCMAudio
from discord import TextChannel
from discord.utils import get
from youtube_dl import YoutubeDL
import requests
import re
import random

# ------ #TODO# ------
# Stop music when game end. (needs ctx)
# Loop through questions.... (creates a bug with on_reaction_add - too many things for a single message)
#

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='.',intents=intents)
# client.remove_command('help')

# List of categories
category_dict = {'General Knowledge' : 9, 'Books' : 10, 'Film' : 11, 'Music' : 12, 'Musicals & Theatres' : 13, 'Television' : 14 ,'Video Games' : 15
,'Board Games' : 16,'Science & Nature' : 17,'Computer Science' : 18,'Mathematics' :19 ,'Mythology' : 20 ,'Sports' : 21, 'Geography' : 22,'History':23
,'Politics':24,'Art':25,'Celebrities' :26,'Animals':27,'Vehicles':28,'Anime':31}


@client.command()
async def categories(ctx):
    await ctx.send("The following categories are available for trivia")
    await ctx.send("General Knowledge\nBooks\nFilm\nMusic\nMusicals & Theatres\nTelevision\nVideo Games\nBoard Games\nScience & Nature\nComputer Science")
    await ctx.send("Mathematics\nMythology\nSports\nGeography\nHistory\nPolitics\nArt\nCelebrities\nAnimals\nVehicles\nAnime")

#***********************************************#

@client.command()
async def sus(ctx):
    await ctx.send("Sacha")

@client.command()
async def tom(ctx):
    await ctx.send("I failed math three times!! \n0-5 btw")

    #mateus
@client.command()
async def antivax(ctx):
    await ctx.send("Mateus : GoVerNment is GonNA CoNtRoL mE")

#******************************************************************#

@client.event
async def on_ready():
    clients = []

    cwd = os.getcwd()

    # Create file "classroom(number).txt"
    file_name = os.path.join(cwd, "clients.txt")

    txt_file = open(file_name, "w")

    #
    clients_file = open("clients.txt","w",encoding="utf-8")
    for member in client.get_all_members():
        member_data = member.name
        raw_data = member_data+','+"0"+',,'
        try:
            txt_file.write(str(raw_data)+'\n')
        except:
            print(member.name + "Cant play lol")


    txt_file.close()

    resp = "Data file generated"
    print(resp)

'''
    for member in 
        clients += member
        print(member)
    print(clients)
    '''

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

# Greet new suer

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

#Send message when a user leaves

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

# Respond with latency in ms

@client.command()
async def ping(ctx):
    await ctx.send(f"pong: {round(client.latency*1000)}ms" )

# respond to Hi

@client.command()
async def hi(ctx):
    await ctx.send("Hello I am BeanerBot.")


# command to stop voice
@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")
# Start a game of trivia

@client.command()
async def trivia(ctx,args):
    global category_dict
    print("Passed argument: " + args)

    if category_dict.get(args):
        url = 'https://opentdb.com/api.php?amount=1&category='+str(category_dict.get(args)) +'&difficulty=medium&type=multiple'
        req = urllib.request.Request(url)

        try:
            ##parsing response
            r = urllib.request.urlopen(req).read()
            cont = json.loads(r.decode('utf-8'), object_hook=lambda d: SimpleNamespace(**d))
            counter = 0
            channel = ctx.message.author.voice.channel
            voice = get(client.voice_clients, guild=ctx.guild)
            if voice and voice.is_connected():
                await voice.move_to(channel)
            else:
                voice = await channel.connect()

            YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
            FFMPEG_OPTIONS = {
                'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            voice = get(client.voice_clients, guild=ctx.guild)

            song = "https://www.youtube.com/watch?v=PCIvOGveIK0"
            if not voice.is_playing():
                with YoutubeDL(YDL_OPTIONS) as ydl:
                    info = ydl.extract_info(song, download=False)
                song_URL = info['url']
                voice.play(FFmpegPCMAudio(song_URL, **FFMPEG_OPTIONS))
                voice.is_playing()
        except Exception as e:
            print(e)
            #await ctx.send("For music, join a channel!")

        for question in cont.results:
            counter += 1
            print("Category:" + args +"\n Question:"+question.question+ "\nAwnsers:"+ str(question.incorrect_answers))
            print("____________")

            embed = discord.Embed(
            color=discord.Color.green()
            )
            embed.title= 'Trivia!'
            embed.add_field(name="Category", value=(args), inline="False")
            embed.add_field(name="Type", value=(question.type), inline="False")
            embed.add_field(name="Difficulty", value=(question.difficulty), inline="False")
            message = await ctx.send(embed=embed)
            i = 1
            while i > 0:

                time.sleep(1)

                embed.title= ('Trivia! '+f"{i}s")
                
                await message.edit(embed=embed)
                i -= 1


            embed.title= ('Trivia! Starting...')

            await message.edit(embed=embed)

            await message.delete()

            embed2 = discord.Embed(
            color=discord.Color.green()
            )  

            embed2.title= 'Trivia!'
            embed2.title= question.question
            embed2.add_field(name=("🅰 : "+str(question.incorrect_answers[0])), value="_______", inline="False")
            embed2.add_field(name=("🅱️ : "+str(question.incorrect_answers[1])), value="_______", inline="False")
            embed2.add_field(name=("© : "+str(question.incorrect_answers[2])), value="_______", inline="False")
            embed2.add_field(name=("🌹 : "+str(question.correct_answer)), value="_______", inline="False")

            message2 = await ctx.send(embed=embed2)
            
            await message2.add_reaction("🅰" )
            await message2.add_reaction("🅱️")
            await message2.add_reaction("©")
            await message2.add_reaction("🌹")

    else:
        await ctx.send("Invalid Category!")


def save(user,credits):
    cwd = os.getcwd()

    # Open file "clients.txt" and save to a list
    file_name = os.path.join(cwd, "clients.txt")

    #txt_file = open(file_name, "r+")

    with open('clients.txt', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    print("Opened File.... Saved to data")
    f.close()

    print("Passed variable: "+user)

    i = 0

    for name in data:

            client = re.sub(r'\W+', '', name[0])
            #print(client)
            if client == user:
                print(name[1])
                print("Found user")
                
                socialCredits = int(name[1])
                print(name[1])
                socialCredits += credits
                print(socialCredits)
                name[1] = socialCredits

                ##name[1] = credits
                
                print(name)
                break
            
            i+=1

    #
    clients_file = open("clients.txt","r+",encoding="utf-8")

    with open('clients.txt', 'r+') as f:

        for name in data:

            s = ","
            #s = s.join(name)
            converted_list = [str(element) for element in name]
            joined_string = ",".join(converted_list)
            clients_file.write(joined_string+'\n')


    clients_file.close()
       
@client.command()
async def credits(ctx):
    cwd = os.getcwd()

    # Open file "clients.txt" and save to a list
    file_name = os.path.join(cwd, "clients.txt")

    #txt_file = open(file_name, "r+")

    with open('clients.txt', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    f.close()

    print("Passed variable: "+ctx.message.author.name)

    i = 0

    for name in data:

            client = re.sub(r'\W+', '', name[0])
            #print(client)
            if client == ctx.message.author.name:
                print(name[1])
                print("Found user")
                
                socialCredits = int(name[1])
                print(name[1])


                embed = discord.Embed(
                    color=discord.Color.gold()
                    )  
                embed.title = 'Bank'
                embed.add_field(name=(str(ctx.message.author.name)), value="You have "+name[1]+ " social credits.", inline="False")

                await ctx.send(embed=embed)
                
                print(name)
                break
            
            i+=1



@client.command()
async def test(ctx):
    username = ctx.message.author.name
    if(str(username) == "TheMemer27" or str(username) == "AODA"):
        save(str(username),50)

    else:
        await ctx.send("Youre not admin")

    
@client.event
async def on_reaction_add(reaction, user):
    user_list = []
    if str(user) not in user_list:
        user_list += [user]
    else:
        print("=--=--=-=-=- DUPLICATED =-=-=-=-=")
    
    reactions = reaction.message.reactions
    # DO WHAT YOU WANT HERE 
    if(str(user) != "BeanerBot#0361"):

        print(str(user) +"\t "+ str(reaction))

        if(str(reaction) == "🌹"):
            if (user_list[0] == user):

                print("=========== WINNER MESSAGGE ===============")

                #await reaction.message.delete()
                
                embed = discord.Embed(
                    color=discord.Color.green()
                    )  
                embed.title = 'Winner'
                embed.add_field(name=(str(user)), value="Has won 50 Social Credits!", inline="False")

                await reaction.message.edit(embed=embed)

                await reaction.message.clear_reaction("🅰")
                await reaction.message.clear_reaction("🅱️")
                await reaction.message.clear_reaction("©")
                await reaction.message.clear_reaction("🌹")

                a_string = str(user)
                split_string = str(a_string).split("#", 1)

                substring = split_string[0]
                print(substring)

                save(str(substring),50)

                
        else:
            print("=========== GAME END ===============")

            #await reaction.message.delete()
            
            embed = discord.Embed(
                color=discord.Color.red()
                )  
            embed.title = 'Looser'
            embed.add_field(name=(str(user)), value="Hold this: L", inline="False")

            await reaction.message.edit(embed=embed)

            await reaction.message.clear_reaction("🅰")
            await reaction.message.clear_reaction("🅱️")
            await reaction.message.clear_reaction("©")
            await reaction.message.clear_reaction("🌹")

client.run('ODE2MTc4MDAwMTY3OTYwNjE2.YD3K_w.0jaZ7zEcU3aBkq-UU5j0t2MxXZ4')