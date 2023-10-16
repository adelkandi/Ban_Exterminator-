# Ban Exterminator BOT 
from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
import openai   # Using open ai Gpt 4  as helper 
import io 
import scripts as sc    # Import functions from scripts file 


# Ban_Exterminator : 


load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


intents = discord.Intents.default()
intents.message_content = True
BOT = commands.Bot(command_prefix='!', intents=intents) # Allow commands for this bot 




# Commands Bot usage: 
@BOT.command() 

# Command Functions:
async def kick(ctx,user:discord.Member):
    await sc.kick_moder(ctx,user)

async def ban(ctx, user: discord.Member):
    await sc.ban_moder(ctx,user)
    await sc.auto_ban()
async def warn(user: discord.Member,message,user_id):
    await sc.auto_warn(message,user)     # Auto warning: check ai run True 
    await sc.warn_moder(user_id)        # moderator warning


# Event when Bot sense a message :
@BOT.event


async def on_ready():
    print("We have logged in as {0.user}".format(BOT))    # Show in terminal that the BOT is Login succesfully

async def on_message(message,user):

    # Check the message from channel if its from the same BOT 
    if message.author == BOT.user:
        return                           # Ignore  
    result = sc.check_ai(message)
    if result == True:       
        await message.channel.send("This message breaks community value standards!")

    if message.channel.content == "!Check_war":
        result = sc.check_warn(user)
        await message.channel.send(f"{user.name} the numbers of warnnings you have is: ") # Make update Later when you finnish the check_awarn() function 

    
    await BOT.process_commands(message)  # Make sure to process commands from message 




BOT.run(DISCORD_TOKEN)