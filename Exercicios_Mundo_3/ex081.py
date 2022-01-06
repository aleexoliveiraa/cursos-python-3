'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:                                                                                                                                                
A) Quantos números foram digitados. 
B) A lista de valores, ordenada de forma decrescente.                                                                                          
C) Se o valor 5 foi digitado e está ou não na lista.'''

listanum = []
while True:
    listanum.append(int(input('Digite um número: ')))
    continuar = str(input('Desja continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
print('=' * 45)
print(f'Você digitou {len(listanum)} elementos.')
listanum.sort(reverse=True)
print(f'Os valores em ordem decrescente são {listanum}.')
if 5 in listanum:
    print(f'O número 5 se encontra na lista.')
else:
    print('O número 5 não se encontra na lista.')