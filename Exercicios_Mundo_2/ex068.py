'''Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias 
consecutivas que ele conquistou no final do jogo.'''

from random import randint
v = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ìmpar: [P/I] ')).strip().upper()[0]
        print(f'Você jogou {jogador} e eu {computador}. O total é {total}. ', end='')
        print(f'DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('PARABÉNS, você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    if tipo == 'I':
        if total % 2 != 0:
            print('PARABÉNS, você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')