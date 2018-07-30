import discord
import asyncio

client = discord.Client()

MsgAuthor = None


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith(';;test'):
        await client.send_message(message.channel, 'fuck off neko')
        print("Someone used the ';;test' command")


client.run('')