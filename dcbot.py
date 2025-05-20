import discord
import requests
import json

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']


class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))
  async def on_message(self, message):
    if message.author == self.user:
        return

    if message.content.startswith('$start'):
        await message.channel.send('Welcome!Sush DC bot is here to help you!')
    if message.content.startswith('$meme'):
        await message.channel.send(get_meme())
    if message.content.startswith('$help'):
        await message.channel.send('Commands: $start, $meme')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTM3MzkzOTE3MTY4ODcxMDE4Nw.GoewEe.d4CN3UWhQiQ52BQz7JBq9IHEyDrf4tNiBV14aI') 