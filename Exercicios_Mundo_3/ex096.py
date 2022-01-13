'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a área do terreno.'''


def area(a, b):
    print(f'A área de um terreno com {a}m x {b}m é igual a {a * b}m².')


print('CONTROLE DE TERRENOS')
print('-' * 20)
largura = float(input('Qual a largura? '))
comprimento = float(input('Qual o comprimento? '))
area(largura, comprimento)
