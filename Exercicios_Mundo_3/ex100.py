'''Faça um programa que tenha uma lista chamada números e duas funções chamadas
sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los
dentro da lista e a segunda função vai mostrar a soma entre todos os valores
pares sorteados pela função anterior.'''

from random import randint
from time import sleep


def sorteia(sorteio):
    print(f'Sorteando 5 valores na lista: ', end='')
    for c in range(0, 5):
        num = randint(0, 10)
        sorteio.append(num)
        print(f'{num} ', end='')
        sleep(0.5)

def somaPar(números):
    soma = 0
    for n in números:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {números} temos {soma}')

lista = []
sorteia(lista)
print()
somaPar(lista)
