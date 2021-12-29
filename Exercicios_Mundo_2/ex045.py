# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(''' Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua opção? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 12)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 12)
if computador == 0: # computador jogou pedra
    if jogador == 0: # jogador jogou pedra
        print('EMPATE')
    elif jogador == 1: # jogador jogou papel
        print('PARABÉNS! Você ganhou!')
    elif jogador == 2: # joagdor jogou tesoura
        print('VOCÊ PERDEU!')
    else:
        print('OPÇÃO INVÁLIDA, Jogue novamente!')
elif computador == 1: # computaodr jogou papel
    if jogador == 0: # jogador jogou pedra
        print('VOCÊ PERDEU!')
    elif jogador == 1: #jogador jogou papel
        print('EMPATE')
    elif jogador == 2: # jogador jogou tesoura
        print('PARABÉNS! Você ganhou!')
    else:
        print('OPÇÃO INVÁLIDA, Jogue novamente!')
elif computador == 2: # computador jogou tesoura
    if jogador == 0: # jogador jogou pedra
        print('PARABÉNS! Você ganhou!')
    elif jogador == 1: # jogador jogou papel
        print('VOCÊ PERDEU!')
    elif jogador == 2: # jogador jogou tesoura
        print('EMPATE')
    else:
        print('OPÇÃO INVÁLIDA, Jogue novamente!')