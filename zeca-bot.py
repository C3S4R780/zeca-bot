import os
import discord
from discord.ext import commands
from datetime import datetime
from time import time, sleep
from apiKeys import BOTTOKEN

# Global variables
# intents = discord.Intents.default()  # Setup bot intents
# intents.message_content = True
# client = commands.Bot(command_prefix="/", intents=intents)
client = commands.Bot(command_prefix="/")  # Create bot client
ONE_HOUR = 60 * 60  # seconds
ONE_DAY = 24 * ONE_HOUR  # seconds


async def send_zeca():
    channel = client.get_channel(997879947874021428)
    await channel.send(file=discord.File('zeca.png'))


# --- Events ---
@client.event
async def on_ready():
    horario_atual = time()
    while horario_atual <= horario_atual + ONE_DAY:
        hoje = datetime.today()
        if hoje.weekday() == 2:  # Zeca-feira (Quarta-feira)
            if hoje.hour == 18:
                await send_zeca()
                sleep(ONE_DAY)
            else:
                sleep(5 * 60)  #  minutos


client.run(BOTTOKEN)