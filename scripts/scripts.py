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
    else: 
        pass 

# Manual warning function: 
def warn_moder(message):
    return 

# Manual ban function:
async def ban_moder(ctx, user: discord.Member):  
    if ctx.author.guild_permissions.ban_members :            # Check if the user has the ban permission.
        await ctx.guild.ban(user)
        await ctx.send(f"{user.name} has been banned from this server!")
    else:
        await ctx.send("You Dont have the Permission to ban members")

# Manual Kick function:
async def kick_moder(ctx, user: discord.Member):
    if ctx.author.guild_permission.kick_members:
        await ctx.guild.kick(user)
        await ctx.send(f"{user.name} has been kicked from the server!")
    else:
        await ctx.send(f"You Dont have Permession to kick members")


# Automatic warn function
def auto_warn(message):
    if check_ai(message) == True : 
        return 

# Automatic ban function 
def auto_ban(message):
    return


# Function check warnings by user or admin 
def check_warn():
    return
