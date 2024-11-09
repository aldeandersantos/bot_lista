import random
import re

def tratar_lista(texto):
    match = re.search(r"⚽Linha:\s+((?:\d+\s-\s[^\n]+\n?)+)", texto)
    if match:
        linha_texto = match.group(1)
        
        jogadores = []
        for linha in linha_texto.strip().split("\n"):
            num, nome = linha.split(" - ", 1)
            jogadores.append(f"{num} - {nome.title()}") 
        
        return " ".join(jogadores)
    return "Não foi possível encontrar a lista de jogadores."

def criar_times(jogadores):
    random.shuffle(jogadores)
    time1 = jogadores[:6]
    time2 = jogadores[6:12]
    time3 = jogadores[12:]
    return time1, time2, time3
