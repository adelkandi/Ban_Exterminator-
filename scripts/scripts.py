# Function that runs the bots 
import discord
import requests
import openai


# check message 
def check_ai(message):
    responce = openai.Completion.creat(
        engine = "text-davenci-004",
        prompt = f"check this message if it breaks community value standards and just response with True or Falsed nothing else; the message is:{message}",
        max_tokens = 100,
        n = 1,
        temperature = 0.5,
        stop = None,)
    result = responce.choice[1].text.strip()
    if result == True: 
        return result 


def warn_moder(message):
    return 


async def ban_moder(ctx, user: discord.Member):  
    if ctx.author.guild_permissions.ban_members :            # Check if the user has the ban permission.
        await ctx.guild.ban(user)
        await ctx.send(f"{user.name} has been banned from this server!")
    else:
        await ctx.send("You Dont have the Permission to ban members")

    return

async def kick_moder():
    return


def auto_warn(message):
    return


def auto_ban(message):
    return

