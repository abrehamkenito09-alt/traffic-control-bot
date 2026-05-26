import discord
from discord.ext import commands
import os

# ቦቱ መልዕክቶችን እንዲያነብ ይፈቅዳል
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'ቦቱ ኦንላይን ሆኗል: {bot.user}')

# የቦቱን ቶከን ከRailway Variables ውስጥ ይወስዳል
bot.run(os.environ['DISCORD_TOKEN'])
