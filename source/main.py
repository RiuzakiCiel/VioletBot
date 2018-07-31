import discord
import asyncio
import os

client = discord.Client()

if not os.path.isfile("bot_token.txt"):
    print("Please insert your bot token")
    token = input()
    token_txt = open(r"bot_token.txt", "a+")
    token_txt.write(token)
    token_txt.close

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith(';;ban'):
        await client.send_message(message.channel, 'Proccessing ban...')
        print("Someone used the ;;ban command")
    if message.content.startswith(';;r1'):
        await client.send_message(message.channel, 'Do not impersonate people. You can swear in this server but do not use any racial/sexist/etc. (you know the drill) words.')
        print("Someone used the ;;r1 command")
    if message.content.startswith(';;r2'):
        await client.send_message(message.channel, "Keep the channels on topic this applies to voice channels too!")
        print("Someone used the ;;r2 command")
    if message.content.startswith(';;r3'):
        await client.send_message(message.channel, "Read the description of the chat you're in to make sure you are not breaking any rules there, we are not super strict and let a lot just sliping by, but you don't want to have the chance to be kicked. This applies to voice channels too!")
        print("Someone used the ;;r3 command")
    if message.content.startswith(';;r4'):
        await client.send_message(message.channel, "We do not tolerate useless @'s or @'s to random people. Do not tag mods unless it's really necessary!")
        print("Someone used the ;;r4 command")
    if message.content.startswith(';;r5'):
        await client.send_message(message.channel, "Do not tease people with there spelling of words, only if they really ask for help.")
        print("Someone used the ;;r5 command")
    if message.content.startswith(';;r6'):
        await client.send_message(message.channel, "DO NOT SPAM!!!!! Spamming is one of the easiest ways to get a warning/ban.")
        print("Someone used the ;;r6 command")
    if message.content.startswith(';;r7'):
        await client.send_message(message.channel, "Don't drama. it's as simple as that.")
        print("Someone used the ;;r7 command")
    if message.content.startswith(';;r8'):
        await client.send_message(message.channel, "This is an english speaking server, don't randomly start talking in Spanish!")
        print("Someone used the ;;r8 command")
    if message.content.startswith(';;taco'):
        await client.send_message(message.channel, "Do you like taco's?")
        print("Someone used the ;;taco command")




token_txt = open(r"bot_token.txt", "r")
token = token_txt.read()
client.run(token)
token_txt.close