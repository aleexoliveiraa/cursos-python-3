'''Faça um programa que tenha uma função chamada contador(), que receba
três parâmetros: início, fim e passo. Seu programa tem que realizar três
contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''

from time import sleep


def contador(inicio, fim, passo):
    print('-=' * 15)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(3)
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= passo
        print('FIM!')
    print('-=' * 15)


contador(10, 0, 2)
contador(1, 15, 3)
print('-=' * 15)
print('Agora é a sua vez: ')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
