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
    if message.content.startswith(';;test'):
        await client.send_message(message.channel, 'test')
        print("Someone used the ';;test' command")

token_txt = open(r"bot_token.txt", "r")
token = token_txt.read()
client.run(token)
token_txt.close