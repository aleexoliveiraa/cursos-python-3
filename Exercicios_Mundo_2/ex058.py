'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” 
em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar 
até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''
from random import randint
computador = randint(0, 10)
print('Vou pensar num número entre 0 e 10 será que você consegue acertar?')
jogador = int(input('Digite seu palpite: '))
tentativas = 0
while jogador != computador:
    if jogador < computador:
        print('Mais... Tente outra vez!')
        jogador = int(input('Em qual número pensei? '))
        tentativas += 1
    if jogador > computador:
        print('Menos... Tente outra vez!')
        jogador = int(input('Em qual número pensei? '))
        tentativas += 1
print(f'PARABÉNS! Você acertou com {tentativas} tetativas!')
