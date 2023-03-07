# colemanbot.py

import os
import discord
import random

from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
client = discord.Client(intents=intents)
TOKEN = os.getenv('DISCORD_TOKEN')

@client.event
async def on_message(self, message):
    if message.author == self.user:
        return


@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        await message.channel.send(random.sample(list(open('quotes.txt'))))
    
client.run(TOKEN)
