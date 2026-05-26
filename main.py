import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'ቦቱ ኦንላይን ሆኗል: {bot.user}')

# የራስዎን ኮዶች እዚህ መጻፍ ይችላሉ
bot.run(os.environ['DISCORD_TOKEN'])
