# Ban Exterminator BOT 
from dotenv import load_dotenv
import os
import requests
import discord
import openai   # Using open ai Gpt 3  as helper 
import io 

# Ban_Exterminator : 


load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
