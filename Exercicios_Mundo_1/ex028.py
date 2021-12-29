from random import randint
from time import sleep
computador = randint(0, 5) # Gera um número aleatório entre 0 e 5
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tende advinhar qual é...')
print('-=-' * 20)
jogador = int(input('Em qual número pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print(f'PARABÉNS! Eu pensei no número {computador} e você acertou!')
else:
    print(f'ERROU! Eu pensei em {computador}!')
