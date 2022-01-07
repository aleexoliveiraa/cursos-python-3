'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 
6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

from random import randint
from time import sleep

print('-=' * 30)
print('                    JOGO DA MEGA SENA')
print('-=' *30)
jogo = []
total_jogos = []
quantidade = int(input('Quantos jogos deseja fazer? '))
total = 1
while total <= quantidade:
    contador = 0
    while True:
        número = randint(1, 60)
        if número not in jogo:
            jogo.append(número)
            contador += 1
        if contador >= 6:
            break
    jogo.sort()
    total_jogos.append(jogo[:])
    jogo.clear()
    total += 1
print(f'-=' * 4, 'SORTEANDO NÚMERO', '-=' * 4)
for indice, lista in enumerate(total_jogos):
    print(f'Jogo {indice + 1}: {lista}')
    sleep(0.5)