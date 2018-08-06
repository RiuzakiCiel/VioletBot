import discord
import asyncio
import os
import random
import linecache
from discord.ext import commands

bot = commands.Bot(command_prefix=";;")

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

@bot.event #Startup message for host
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context=True) 
async def r1(ctx): #R1 command
    await bot.say(linecache.getline("../txt_files/rules.txt", 1))
    print(ctx.message.author, "used the r1 command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
async def r2(ctx): #R2 command
    await bot.say(linecache.getline("../txt_files/rules.txt", 2))
    print(ctx.message.author, "used the r2 command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
async def r3(ctx): #R3 command
    await bot.say(linecache.getline("../txt_files/rules.txt", 3))
    print(ctx.message.author, "used the r3 command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
async def r4(ctx): #R4 command
    await bot.say(linecache.getline("../txt_files/rules.txt", 4))
    print(ctx.message.author, "used the r4 command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
async def r5(ctx): #R5 command
    await bot.say(linecache.getline("../txt_files/rules.txt", 5))
    print(ctx.message.author, "used the r5 command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
async def r6(ctx): #R6 command
    await bot.say(linecache.getline("../txt_files/rules.txt", 6))
    print(ctx.message.author, "used the r6 command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
async def r7(ctx): #R7 command
    await bot.say(linecache.getline("../txt_files/rules.txt", 7))
    print(ctx.message.author, "used the r7 command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
async def r8(ctx): #R8 command
    await bot.say(linecache.getline("../txt_files/rules.txt", 8))
    print(ctx.message.author, "used the r8 command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
async def naru(ctx): #Naru command
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
    RNG = random.randint(1, 19)
    await bot.say(linecache.getline("../txt_files/mantis.txt", RNG))
    print(ctx.message.author, "used the mantis command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
async def ban(ctx, member: discord.Member):
    if ctx.message.author.server_permissions.administrator:
        await bot.ban(member)
        fmt = "{0.mention} is now banned!"
        await bot.send_message(ctx.message.channel, fmt.format(member))
        print(ctx.message.author, "banned", member)
    else:
        await bot.say("You don't have permissions to use this command!")
        print(ctx.message.author, "tried to ban", member, "without permissions!")

@bot.command(pass_context=True)
async def kick(ctx, member: discord.Member):
    if ctx.message.author.server_permissions.administrator:
        await bot.kick(member)
        fmt = "{0.mention} is now kicked"
        await bot.send_message(ctx.message.channel, fmt.format(member))
        print(ctx.message.author, "kicked", member)
    else:
        await bot.say("You don't have permissions to use this command!")
        print(ctx.message.author, "tried to kick", member, "without permissions!")

token_txt = open(r"../txt_files/bot_token.txt", "r")
token = token_txt.read()
bot.run(token)
token_txt.close