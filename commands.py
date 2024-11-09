import re
import discord
from discord import app_commands
from utils import criar_times

async def times(interaction: discord.Interaction, lista: str):
    jogadores = re.findall(r'\d+\s-\s([a-zA-ZÀ-ÿ\s]+)', lista)

    if len(jogadores) < 18:
        await interaction.response.send_message("Por favor, forneça pelo menos 18 nomes para formar três times de 6 jogadores.")
        return

    time1, time2, time3 = criar_times(jogadores)
    times = [time1, time2, time3]
    resposta = ""
    for idx, time in enumerate(times, start=1):
        resposta += f"**Time {idx}**\n" + "\n".join([f"**{i+1}.** {jogador}" for i, jogador in enumerate(time)]) + "\n\n"
    
    await interaction.response.send_message(resposta)

def setup_comandos(bot):
    bot.tree.add_command(app_commands.Command(name="times", description="Cria 3 times de 6 jogadores com base em uma lista fornecida", callback=times))
