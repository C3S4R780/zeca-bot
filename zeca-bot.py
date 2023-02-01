# Imports
import os
import discord
import pytz
from discord.ext import commands, tasks
from datetime import datetime
from keep_alive import keep_alive
from utils import generate_status

# Global variables
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="/", intents=intents)
sent = False

# Loop function every 30 seconds
@tasks.loop(seconds=30, reconnect=True)
async def zeca_timer():
    global sent

    # Data e hora atual, com UTC correto (-3)
    hoje = datetime.now(pytz.timezone('America/Sao_Paulo'))
    status = generate_status(hoje)

    if hoje.weekday() == 2:  # 2 = Zeca-feira (Quarta-feira)
        if hoje.hour == 8 and not sent:
            channels = [997879947874021428, 821937691167162382]
            for channel_id in channels:
                channel = client.get_channel(channel_id)
                msg = await channel.send("@everyone",
                                         file=discord.File('zeca.png'))
                await msg.add_reaction("<:zeca:1069693872713781268>")
            sent = True
        if hoje.hour >= 8 and sent:
            status = "Feliz zeca-feira!"
    else:
        sent = False

    # Change bot status
    await client.change_presence(activity=discord.Game(name=status))


# --- Events ---
@client.event
async def on_ready():

    # Start loop
    zeca_timer.start()

# Cheesing replit timeout time
keep_alive()

# Handle discord rate limiting the bot
try:
    client.run(os.environ['BOTTOKEN'])
except discord.errors.HTTPException as e:
    if e.status == 429:
        print("RATE LIMITED - RESTARTING...")
        os.system("python restarter.py")
        os.system('kill 1')