# Ban Exterminator BOT 
from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
import openai   # Using open ai Gpt 3  as helper 
import io 
import scripts as sc    # Import functions from scripts file 


# Ban_Exterminator : 


load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


intents = discord.Intents.default()
intents.message_content = True
intents.ban_members = True   # Unable the ban intents for Bot 
BOT = discord.Client(intents=intents)




# Commands Bot usage: 
@BOT.command() 

async def kick(ctx,user:discord.Member):
    await sc.kick_moder(ctx,user)
async def ban(ctx, user: discord.Member):
    return                                  # I will add next time a system of 3 warnings then ban automatically;




# Event when Bot sense a message :
@BOT.event


async def on_ready():
    print("We have logged in as {0.user}".format(BOT))    # Show in terminal that the BOT is Login succesfully

async def on_message(message):

    # Check the message from channel if its from the same BOT 
    if message.author == BOT.user:
        return                           # Ignore  
    result = sc.check_ai(message)
    if result == True:       
        await message.channel.send("This message breaks community value standards!")

    await BOT.process_commands(message)  # Make sure to process commands from message 




BOT.run(DISCORD_TOKEN)