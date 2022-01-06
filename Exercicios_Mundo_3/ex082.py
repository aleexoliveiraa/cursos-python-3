'''Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares 
e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.'''

lista = list()
listapares = []
listaimpares = list()
while True:
    números = int(input('Digite um número: '))
    lista.append(números)
    if números % 2 == 0:
        listapares.append(números)
    else:
        listaimpares.append(números)
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Foram digitados os números {lista}.')
print(f'Números pares: {listapares}')
print(f'Números ímpares: {listaimpares}')