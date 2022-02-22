import discord
from discord.ext import commands
import requests
import os


class Admintools(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, extension):
        self.client.load_extension(f'cogs.{extension}')

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, extension):
        self.client.unload_extension(f'cogs.{extension}')

    @commands.command()
    @commands.is_owner()
    async def show(self, ctx, amount):
        response = 'Hallo'
        image_url = 'https://vignette.wikia.nocookie.net/lekkerspelen/images/c/c6/Richard.jpg/revision/latest/scale-to-width-down/220?cb=20181203192730&path-prefix=nl'
        img_data = requests.get(image_url).content
        with open('picture.jpg', 'wb') as handler:
            handler.write(img_data)
        await ctx.send(response)

        for x in range(int(amount)):

            await ctx.send(file=discord.File('picture.jpg'))
        os.remove('picture.jpg')

    @commands.command()
    @commands.is_owner()
    async def clear(self, ctx, amount):
        if amount == "all":
            await ctx.channel.purge(limit=999999999999)
        else:
            await ctx.channel.purge(limit=int(amount) + 1)


def setup(client):
    client.add_cog(Admintools(client))