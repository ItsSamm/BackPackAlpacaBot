import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print('bot loaded')

@client.event
async def on_member_join(member):
    channel = client.get_channel(0) #I did define channel Id in my code
    await channel.send("someone has joined")
    print("AYDFYSF")
client.run('REMOVED')