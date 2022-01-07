'''Aprimore o desafio anterior, mostrando no final:   
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.                                                                                                                
C) O maior valor da segunda linha.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = maior = somacoluna = 0
for linha in range(0, 3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para o intervalo [{linha}, {coluna}]: '))
print('=' * 60)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somapares += matriz[linha][coluna]
    print()
print('=' * 60)
print(f'A soma os elementos pares é {somapares}.')
for linha in range(0, 3):
    somacoluna += matriz[linha][2]
print(f'A soma dos elementos da coluna 3 é {somacoluna}.')
for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz [1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f'O maior elemento da linha 2 é {maior}.')
