import os
import discord
from dotenv import load_dotenv

load_dotenv() 

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        channel = discord.utils.get(client.get_all_channels(), name='ziks-bot')
        await channel.send(f'{member.name} has joined the voice channel {after.channel.name}')



client.run(os.getenv("TOKEN"))