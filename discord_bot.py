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
# FIX SAVE SCORE (Lists gets saved within a list)
# Stop music when game end.
# Loop through questions....
#

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='.',intents=intents)
# client.remove_command('help')

# List of categories
category_dict = {'General Knowledge' : 9, 'Books' : 10, 'Film' : 11, 'Music' : 12, 'Musicals & Theatres' : 13, 'Television' : 14 ,'Video Games' : 15
,'Board Games' : 16,'Science & Nature' : 17,'Computer Science' : 18,'Mathematics' :19 ,'Mythology' : 20 ,'Sports' : 21, 'Geography' : 22,'History':23
,'Politics':24,'Art':25,'Celebrities' :26,'Animals':27,'Vehicles':28,'Anime':31}

#***********************************************#
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
    await ctx.send("I failed math three times!! \n0-5 btw")


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
    await ctx.send("Mateus : GoVerNment is GonNA CoNtRoL mE")

@client.command()
async def evan(ctx):
    await ctx.send("The tax avoider 👨🏾‍🌾.")

# REMOVE WHEN DONE
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
        raw_data = [member_data,"","",""]
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

'''
@client.command()
async def help(ctx):
    embed = discord.Embed(
        color=discord.Color.orange()
    )
    embed.set_author(name='Help')
    embed.add_field(name=".trivia", value='Starts a quick game of Trivia', inline="False")
    
    await ctx.send(embed=embed)
'''
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
        except:
            await ctx.send("For music, join a channel!")

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
    #print(data)

    f.close()

    print("Passed variable: "+user)

    i = 0

    for name in data:

            client = re.sub(r'\W+', '', name[0])
            #print(client)
            if client == user:
                print(name)
                print("Found user")

                name[1] = credits

                print(name)
                break
            
            i+=1

            print(i)


            #print(re.sub('[^a-zA-Z]+', '', name[0]))

    #
    clients_file = open("clients.txt","r+",encoding="utf-8")

    with open('clients.txt', 'r+') as f:
        
        '''
        write = csv.writer(f) 
        #write.writerows(name)
        write.writerows(map(lambda x: [x], data))
        '''
        for name in data:
            clients_file.write(str(name)+'\n')


    clients_file.close()
       



@client.command()
async def test(ctx):
    username = ctx.message.author.name
    if(str(username) == "TheMemer27"):
        save(str(username),50)

    else:
        await ctx.send("Youre not admin")

    #
    '''
    clients_file = open("clients.txt","w",encoding="utf-8")
    for member in client.get_all_members():
        print(member.name)
        member_data = member.name
        #print(repr(member_data))
        raw_data = [member_data,"","",""]
        try:
            txt_file.write(str(raw_data)+'\n')
        except:
            print("Cant play lol")


    txt_file.close()
    '''
    
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
            
            
            #new(user)


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


client.run('ODE2MTc4MDAwMTY3OTYwNjE2.YD3K_w.0jaZ7zEcU3aBkq-UU5j0t2MxXZ4')