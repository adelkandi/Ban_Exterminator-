# Function that runs the bots 
import discord
import requests
import openai
import json


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


#####################################
# Helper functions for warnings : 
warnings = {}
def load_warnings():
    try:
        with open("warnings.json","r") as file:
            json.load(file)
    except FileNotFoundError:
        return{}
    
def save_warnings():
    with open("warnings.json","w") as file : 
        json.dump(warnings, file,indent=4)

def add_warnings(user_id):
    user_id_str = str(user_id)
    warnings[user_id_str] = warnings.get(user_id_str,0) + 1
    save_warnings()



#####################################
# Manual warning function: 

async def warn_moder(user_id):
    add_warnings(user_id)
    return f"User {user_id} has been warned!!!, Total warnings{check_warn(user_id)}"

#async def warn_moder(ctx, user:discord.Member):
#    if ctx.author.guild_permession.warn_members:
#        await ctx.send(f"{user.name} Has been warned!")
#        with open("warnings.json","r") as file:
#            warnings = json.load(file)
#        with open("warnings.json","w") as file:
#            return
            

#    else: 
#        await ctx.send("You Dont have permession to warn members")


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
def auto_warn(message,user_id,user: discord.Member):
    if check_ai(message) == True : 
        add_warnings(user_id)
        return f"User {user.name} has been warned!!, Total warnings {check_warn(user_id)}"

# Automatic ban function 
async def auto_ban(message,ctx,user_id,user: discord.Member):
    totalwarnings = check_warn(user_id)
    if totalwarnings == 3 :
        await ctx.guild.ban(user_id)

    return f"User {user_id} has been banned from this server!!"


# Function check warnings by user or admin 
def check_warn(user_id):
    with open("warnings.json","r") as file :
        warnings = json.load(file)
    return warnings.get(str(user_id), 0)
   