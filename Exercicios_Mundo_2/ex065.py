'''Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

continuar = 'S'
quantidade = soma = média = 0
maior = menor = 0
while continuar in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quantidade += 1
    if quantidade == 1:
        maior = menor = num
    else:
        if num < maior:
            menor = num
        if num > maior:
            maior = num
    continuar = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
média = soma / quantidade
print(f'Você digitouu {quantidade} e a média é {média:.2f}.')
print(f'O maior número digitado foi {maior} e o menor {menor}.')