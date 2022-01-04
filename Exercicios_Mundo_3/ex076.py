'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

produtos = ('SmartTV', 2541.58,
            'Notebook', 2599.99,
            'Mouse', 54.90,
            'HD Externo', 699.89,
            'Memória DDR4', 789.59,
            'Headphone', 1190.59)
print('=' * 40)
print(f'{"Listagem de Preços":^40}')
print('=' * 40)
for posicao in range(0, len(produtos)):
    if posicao % 2 == 0:
        print(f'{produtos[posicao]:.<30}', end='')
    else:
        print(f'R${produtos[posicao]:>8.2f} ')
print('=' * 40)
