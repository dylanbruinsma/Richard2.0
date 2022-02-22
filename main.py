import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            user = await client.fetch_user(211121425589862400)
            await user.send("pong")


client = MyClient()
client.run('NzczMTg5MjE0ODExNTg2NTYy.X6FmkQ.EJN4Xca3E9CS4gcFqzp9_83c4kE')
