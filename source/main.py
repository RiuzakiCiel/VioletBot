import discord
import asyncio
import os
import random
from discord.ext import commands

bot = commands.Bot(command_prefix=";;")

if not os.path.isfile("bot_token.txt"): #Authentication stuff
    print("Please insert your bot token")
    token = input()
    token_txt = open(r"bot_token.txt", "a+")
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
    await bot.say("Do not impersonate people. You can swear in this server but do not use any racial/sexist/etc. (you know the drill) words.")
    print(ctx.message.author, "used the r1 command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
async def r2(ctx): #R2 command
    await bot.say("Keep the channels on topic. this applies to voice channels too!")
    print(ctx.message.author, "used the r2 command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
async def r3(ctx): #R3 command
    await bot.say("Read the description of the chat you're in to make sure you are not breaking any rules there, we are not super strict and let a lot just slip by, but you don't want to have the chance to be kicked. This applies to voice channels too!")
    print(ctx.message.author, "used the r3 command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
async def r4(ctx): #R4 command
    await bot.say("We do not tolerate useless @'s or @'s to random people. Do not tag mods unless it's really necessary!")
    print(ctx.message.author, "used the r4 command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
async def r5(ctx): #R5 command
    await bot.say("Do not tease people with their spelling of words, only if they really ask for help.")
    print(ctx.message.author, "used the r5 command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
async def r6(ctx): #R6 command
    await bot.say("Do not spam. Spamming is one of the easiest ways to get a warning/ban.")
    print(ctx.message.author, "used the r6 command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
async def r7(ctx): #R7 command
    await bot.say("Don't do drama. it's as simple as that.")
    print(ctx.message.author, "used the r7 command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
async def r8(ctx): #R8 command
    await bot.say("This is an english speaking server, so keep communicating to that language.")
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
async def ban(ctx, member: discord.Member):
    if ctx.message.author.server_permissions.administrator:
        await bot.ban(member)
        fmt = "{0.mention} is now banned!"
        await bot.send_message(ctx.message.channel, fmt.format(member))
        print(ctx.message.author, "banned", member)
    else:
        await bot.say("You don't have permissions to use this command!")
        print(ctx.message.author, "tried to ban", member, "without permissions!")

token_txt = open(r"bot_token.txt", "r")
token = token_txt.read()
bot.run(token)
token_txt.close