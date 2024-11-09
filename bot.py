import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from commands import setup_comandos

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Comandos de barra sincronizados: {len(synced)} comandos")
    except Exception as e:
        print(f"Erro ao sincronizar comandos: {e}")

setup_comandos(bot)

bot.run(TOKEN)
