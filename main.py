import discord
import os
import datetime
from discord.ext import commands

client = commands.Bot(commands.when_mentioned_or('pp '))

client.load_extension('cogs.Tools')



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you",
                                                           start=datetime.datetime.utcfromtimestamp(0)))


client.run(os.environ.get('bottoken'))
