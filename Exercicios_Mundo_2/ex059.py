'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opção = 0
while opção != 5:
    print('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR QUE
    [4] NOVOS NÚMEROS
    [5] SAIR''')
    opção = int(input('Opção: '))
    if opção == 1:
        print(f'A soma de {n1} e {n2} é iual a {n1 + n2}.')
    elif opção == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}.')
    elif opção == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        elif n2 > n1:
            print(f'{n2} é maior que {n1}')
        else:
            print(f'Os números são IGUAIS!')
    elif opção == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opção == 5:
        print('Programa encerrado! Obrigado por usar!')
    else:
        print('Opção inválida. Tente Novamente!')

