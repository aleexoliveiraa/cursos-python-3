'''Crie um programa onde o usuário possa digitar vários valores numéricos 
e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

listanum = []
while True:
    número = int(input('Digite um número: '))
    if número not in listanum:
        listanum.append(número)
        print('Valor adicionado à lista!')
    else: 
        print('Número duplicado. Não adicionado à lista.')
    continuar = str(input('Deseja continuar a digitar valores? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Foram adicionados à lista os números: {sorted(listanum)}.')