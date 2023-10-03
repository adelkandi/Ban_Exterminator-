# Function that runs the bots 
import discord
import requests
import openai



def check_ai(message):
    responce = openai.Completion.creat(
        engine = "text-davenci-004",
        prompt = "check this message if it breaks community value standards and just response with True or Falsed nothing else",
        max_tokens = 100,
        n = 1,
        temperature = 0.5,
        stop = None,)
    result = responce.choice[1].text.strip()
    if result == True: 
        return result 


def warn_moder(message):
    return 

def ban_moder(message):
    return

def auto_warn(message):
    return

def auto_ban(message):
    return
