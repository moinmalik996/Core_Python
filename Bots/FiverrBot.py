import discord
from discord.ext import commands
import random

token = "ODI1OTk1NzEyNTQ1MTYxMjE2.YGGCdA.fmSfLMVZ-Rum-J5s0KCHGewwEXE"

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print("Bot is Ready")

@client.event
async def on_message(message):
    print(message.content)


client.run(token)
