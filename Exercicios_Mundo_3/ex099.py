'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

from time import sleep


def maior(*numeros):
    print('-=' * 30)
    print('Analisando os valores passados...')
    maiorque = cont = 0
    for valor in numeros:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maiorque = valor
        else:
            if valor > maiorque:
                maiorque = valor
        cont += 1
    print(f'O maior valor informado foi {maiorque}.')
    print(f'Ao todo foram informados {cont}.')

maior(1, 2, 5, 19, 0, 3, 4)
maior(6, 5, 11, 0, 2, 7)
maior(6)
maior()

