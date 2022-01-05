'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

lista = []
for contador  in range(0, 5):
    n = int(input('Digite um número: '))
    if contador == 0 or n > lista[-1]:
        lista.append(n)
    else:
        posição = 0
        while posição < len(lista):
            if n < lista(posição):
                lista.insert(posição, n)
                break
            posição += 1
print(f'Os valores digitados foram {lista}.')
