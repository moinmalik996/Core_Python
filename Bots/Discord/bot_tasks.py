import discord
from discord.ext import commands, tasks
from itertools import cycle

token = "ODI1OTk1NzEyNTQ1MTYxMjE2.YGGCdA.fmSfLMVZ-Rum-J5s0KCHGewwEXE"

client = commands.Bot(command_prefix='.')
status = cycle(['status_1', 'stuatus_2', 'status_3'])

@client.event
async def on_ready():
    status_change.start()
    print("Bot is Ready")


@tasks.loop(seconds=10)
async def status_change():
    await client.change_presence(activity=discord.Game(next(status)))


client.run(token)