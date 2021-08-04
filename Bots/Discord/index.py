import discord
from discord.ext import commands
import random

token = "ODI1OTk1NzEyNTQ1MTYxMjE2.YGGCdA.fmSfLMVZ-Rum-J5s0KCHGewwEXE"

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print("Bot is Ready")


# @client.event
# async def on_member_join(member):
#     print(f"{member} has joined")



# @client.event
# async def on_member_remove(member):
#     print(f"{member} has removed")


# @client.command()
# async def ping(ctx):
#     await ctx.send(f"Pong ! {round(client.latency * 1000)}ms")



# @client.command(aliases=["MalikMoin"])
# async def _msgs(ctx, *, question):
#     responses = [
#         'Hi, Whats up.',
#         'How are you doing',
#         'I am a bot',
#         'You are doing wrong',
#         'My owner is Moin Malik'
#     ]

#     await ctx.send(f"{question} \nAnswer : {random.choices(responses)}")


# @client.command()
# async def clear(ctx, amount = 5):
#     await ctx.channel.purge(limit = amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f'Banned {member.mention}')



@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return





client.run(token)

