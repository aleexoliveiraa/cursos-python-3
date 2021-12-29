''' Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''
total = menor = barato = maismil = cont = 0
print('-' * 50)
print('LOJAS OLIVEIRA')
while True:
    produto = str(input('Produto: '))
    preço = float(input('Preço: R$'))
    total += preço
    cont += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    if preço > 1000:
        maismil += 1
    novo = ' '
    while novo not in 'SN':
        novo = str(input('Deseja continuar cadastrando? [S/N] ')).strip().upper()[0]
    if novo == 'N':
        break
print('-=' * 30)
print(f'TOTAL DAS COMPRAS'.center(50))
print('-=' * 30)
print(f'O total da compra é R${total:.2f}.')
print(f'Ao todo foram cadastrados {maismil} produtos acima de R$1.000,00')
print(f'O produto de menor valor foi {menor}.')
