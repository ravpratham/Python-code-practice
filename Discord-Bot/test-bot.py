import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix="prt:")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("Connected Successfully")
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return

    elif message.content.startswith('hello'):

        if str(message.author) == "prathamrav":

            # await message.channel.send(f"hello! {message.author}, how are you ")

            com1 = f"What's up {message.author}"
            com2 = "How u doin'"
            com3 = f"YO {message.author}"
            com4 = "How are you my lord"

            commentsList = [com1, com2, com3, com4]

            await message.channel.send(random.choice(commentsList))

client.run("MTEyOTI4NzcxMDc1MDgyMjUwMQ.Gqt5Ba.VC9e88d4x5aCRpG8LjSzCB3d3JGBGMphOq2KEM")
