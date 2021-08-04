import discord
from discord.ext import commands
import random

token = "ODI1OTk1NzEyNTQ1MTYxMjE2.YGGCdA.fmSfLMVZ-Rum-J5s0KCHGewwEXE"

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Hello There'))
    print("Bot is Ready")


client.run(token)