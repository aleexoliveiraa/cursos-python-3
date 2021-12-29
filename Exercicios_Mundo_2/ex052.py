# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um número: '))
cont = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print(f'\033[1;33m{c}\033[m', end=' → ')
        cont += 1
    else:
        print(f'\033[1;31m{c}\033[m', end=' → ')
print(f'\n\033[mO número {numero} foi divisível {cont} vezes.')
if cont == 2:
    print(f'O número é PRIMO')
else:
    print(f'O número NÃO É PRIMO')
    