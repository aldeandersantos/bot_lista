import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from commands import setup_comandos

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Comandos de barra sincronizados: {len(synced)} comandos")
    except Exception as e:
        print(f"Erro ao sincronizar comandos: {e}")
    print(f"Bot conectado como {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if isinstance(message.channel, discord.DMChannel):
        await message.channel.send("Oi! Esta é uma mensagem. Em que posso ajudar?")
    
    await bot.process_commands(message)

setup_comandos(bot)

bot.run(TOKEN)
