<<<<<<< HEAD
#test branch testing
=======
#91 Jogo de Dados em Python
from multiprocessing.sharedctypes import Value
from random import randint
from time import sleep
from operator import itemgetter
jogos = {}
for sorteio in range(1, 5):
    numero = randint(1, 6)
    jogos[f'Jogador:{sorteio}'] = numero
print(f"\n{jogos}")
for jogador, valor in jogos.items():
    print(f"{jogador} tirou {valor} no dado.")
    sleep(1)
print("-"*26)
print(f"{'RANKING DOS JOGADORES':^26}")
print("-"*26)

ranking = {}
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
print(ranking)

for i, v in enumerate(ranking):
    print(f"{i+1}º Lugar: {v[0]} com {v[1]} pontos.")

#teste de merge
#teste push github
#
>>>>>>> main
