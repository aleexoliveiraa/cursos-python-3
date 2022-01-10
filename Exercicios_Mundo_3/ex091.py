'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep
from operator import itemgetter

print('-=' * 30)
jogos = {'Jogador_1': randint(1, 6),
         'Jogador_2': randint(1, 6),
         'Jogador_3': randint(1, 6),
         'Jogador_4': randint(1, 6),
         }
for jogador, jogo in jogos.items():
    print(f'O {jogador} tirou {jogo} no dado.')
    sleep(0.5)
print('-=' * 30)
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
for jogador, jogo in enumerate(ranking):
    print(f'O {jogo[0]} ficou em {jogador + 1}º lugar com {jogo[1]} ')
    sleep(0.5)
