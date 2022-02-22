import discord
import os
import datetime


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="to you",
                                                               start=datetime.datetime.utcfromtimestamp(0)))

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            user = await client.fetch_user(211121425589862400)
            await user.send("pong")


client = MyClient()
client.run(os.environ.get('bottoken'))
