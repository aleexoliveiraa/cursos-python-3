'''Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:     
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

pessoas = list()
dados = list()
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    dados.clear()
    continuar = str(input('Continuar a cadastrar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
print('-=' * 30)
print(f'Ao todo foramc adastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}kg. Foi o peso de ', end='')
for c in pessoas:
    if c[1] == maior:
        print(f'{c[0]} ', end='')
print()
print(f'O menor peso cadastrado foi {menor}. Foi o peso de {menorpeso}')
for c in pessoas:
    if c[1] == menor:
        print(f'{c[0]} ', end='')
