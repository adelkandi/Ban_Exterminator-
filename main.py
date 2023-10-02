# Ban Exterminator BOT 
from dotenv import load_dotenv
import os
import requests
import discord
import openai   # Using open ai Gpt 3  as helper 
import io 
import scripts # Import functions from scripts file 
# Ban_Exterminator : 


load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
BOT = discord.Client(intents=intents)

# Event when Bot sense a message :
@BOT.event


async def on_ready():
    print("We have logged in as {0.user}".format(BOT))    # Show in terminal that the BOT is Login succesfully

async def on_message(message):
    print("just for test")


BOT.run(DISCORD_TOKEN)