import discord
import asyncio
import os
import random
import linecache
import json
from discord.ext import commands

bot = commands.Bot(command_prefix=";;")

bots = 3

if not os.path.isfile("../txt_files/bot_token.txt"): #Authentication stuff
    print("Please insert your bot token")
    token = input()
    token_txt = open(r"../txt_files/bot_token.txt", "a+")
    token_txt.write(token)
    token_txt.close

@bot.event
async def on_member_join(member): #Welcome message
    server = member.server
    fmt = 'Hey {0.mention}, welcome to the {1.name}!\nPlease read the rules and have fun!'
    await bot.send_message(discord.Object(id='458347412910768128'), fmt.format(member, server))
    print(member, "joined the the", server)
    with open("../txt_files/users.json", "r") as f:
        users = json.load(f)
    await update_data(users, member)
    with open("../txt_files/users.json", "w") as f:
        json.dump(users, f)

@bot.event #Startup message for host
async def on_ready():
    await bot.change_presence(game=discord.Game(name="with Yvar's sanity"))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context=True) 
async def r1(ctx): #R1 command
    """Displays rule 1"""
    embed=discord.Embed(title="Rule 1", description=linecache.getline("../txt_files/rules.txt", 1))
    await bot.say(embed=embed)
    print(ctx.message.author, "used the r1 command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
async def r2(ctx): #R2 command
    """Displays rule 2"""
    embed=discord.Embed(title="Rule 2", description=linecache.getline("../txt_files/rules.txt", 2))
    await bot.say(embed=embed)
    print(ctx.message.author, "used the r2 command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
async def r3(ctx): #R3 command
    """Displays rule 3"""
    embed=discord.Embed(title="Rule 3", description=linecache.getline("../txt_files/rules.txt", 3))
    await bot.say(embed=embed)
    print(ctx.message.author, "used the r3 command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
async def r4(ctx): #R4 command
    """Displays rule 4"""
    embed=discord.Embed(title="Rule 4", description=linecache.getline("../txt_files/rules.txt", 4))
    await bot.say(embed=embed)
    print(ctx.message.author, "used the r4 command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
async def r5(ctx): #R5 command
    """Displays rule 5"""
    embed=discord.Embed(title="Rule 5", description=linecache.getline("../txt_files/rules.txt", 5))
    await bot.say(embed=embed)
    print(ctx.message.author, "used the r5 command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
async def r6(ctx): #R6 command
    """Displays rule 6"""
    embed=discord.Embed(title="Rule 6", description=linecache.getline("../txt_files/rules.txt", 6))
    await bot.say(embed=embed)
    print(ctx.message.author, "used the r6 command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
async def r7(ctx): #R7 command
    """Displays rule 7"""
    embed=discord.Embed(title="Rule 7", description=linecache.getline("../txt_files/rules.txt", 7))
    await bot.say(embed=embed)
    print(ctx.message.author, "used the r7 command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
async def r8(ctx): #R8 command
    """Displays rule 8"""
    embed=discord.Embed(title="Rule 8", description=linecache.getline("../txt_files/rules.txt", 8))
    await bot.say(embed=embed)
    print(ctx.message.author, "used the r8 command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
async def naru(ctx): #Naru command
    """Naru command (for science)"""
    RNG = random.randint(0, 2)
    if RNG == 0:
        await bot.say("Cus itsa  SMALL DICK BOY")
    if RNG == 1:
        await bot.say("The creepy thing?")
    if RNG == 2:
        await bot.say("'I need yvar to wake tf up for this'\nNo you don't. Leave me the fuck alone")
    print(ctx.message.author, "used the naru command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
async def gny(ctx): #Gny command
    """Gny command (for science)"""
    RNG = random.randint(0, 2)
    if RNG == 0:
        await bot.say("Ya shaveing smooth and my crack hard to do")
    if RNG == 1:
        await bot.say("Ok hugs mmm u not still u know thinking ur bad right")
    if RNG == 2:
        await bot.say("Clenches butt cheeks so poop doesn't come out")
    print(ctx.message.author, "used the naru command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
async def mantis(ctx): #Mantis command
    """Mantis commmand (for actual science)"""
    RNG = random.randint(1, 19)
    await bot.say(linecache.getline("../txt_files/mantis.txt", RNG))
    print(ctx.message.author, "used the mantis command in the", ctx.message.channel, "channel")

#@bot.command(pass_context=True)
#async def necro(ctx): #Necro command
#    """Sends a picture of Necro"""
#    await bot.send_file(ctx.message.channel, "../imgs/necro.jpg")
#    print(ctx.message.author, "used the necro command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
async def ban(ctx, member: discord.Member): #Ban command
    """Ban a member"""
    if ctx.message.author.server_permissions.administrator:
        await bot.ban(member)
        fmt = "{0.mention} is now banned!"
        await bot.send_message(ctx.message.channel, fmt.format(member))
        print(ctx.message.author, "banned", member)
    else:
        await bot.say("You don't have permissions to use this command!")
        print(ctx.message.author, "tried to ban", member, "without permissions!")

@bot.command(pass_context=True)
async def kick(ctx, member: discord.Member): #Kick command
    """Kick a member"""
    if ctx.message.author.server_permissions.administrator:
        await bot.kick(member)
        fmt = "{0.mention} is now kicked"
        await bot.send_message(ctx.message.channel, fmt.format(member))
        print(ctx.message.author, "kicked", member)
    else:
        await bot.say("You don't have permissions to use this command!")
        print(ctx.message.author, "tried to kick", member, "without permissions!")

@bot.command(pass_context=True)
async def membercount(ctx): #Membercount command
    """Displays the total amount of members"""
    totalmembers = ctx.message.server.member_count-bots
    await bot.say(f"the {ctx.message.server} now has {totalmembers} members!")
    print(ctx.message.author, "used the membercount command in the", ctx.message.channel, "channel")

@bot.event
async def on_message(message):
    with open("../txt_files/users.json", "r") as f:
        users = json.load(f)
    await update_data(users, message.author)
    await add_experience(users, message.author, 5)
    await level_up(users, message.author, message.channel)
    with open("../txt_files/users.json", "w") as f:
        json.dump(users, f)
    await bot.process_commands(message)

async def update_data(users, user):
    if not user.id in users:
        users[user.id] = {}
        users[user.id]["experience"] = 0
        users[user.id]["level"] = 1

async def add_experience(users, user, exp):
    users[user.id]["experience"] += exp

async def level_up(users, user, channel):
    experience = users[user.id]["experience"]
    lvl_start = users[user.id]["level"]
    lvl_end = int(experience ** (1/4))
    if lvl_start < lvl_end:
        await bot.send_message(channel, "{} has leveled up to level {}!".format(user.mention, lvl_end))
        users[user.id]["level"] = lvl_end

#@bot.command(pass_context=True)
#async def rank(ctx, users, user):
#    experience = users[user.id]["experience"]
#    lvl_end = int(experience ** (1/4))
#    await bot.say("{0.name}, you are level {} with {} xp!".format(user.mention, lvl_end, experience))

token_txt = open(r"../txt_files/bot_token.txt", "r")
token = token_txt.read()
bot.run(token)
token_txt.close