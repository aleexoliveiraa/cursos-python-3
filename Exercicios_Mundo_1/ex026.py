# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip()
quantidade = frase.count('A')
posição_1 = frase.find('A') + 1
posição_final = frase.rfind('A') + 1
print(f'A frase digitada possui {quantidade} letras')
print(f'Sua primeira aparição é na posição {posição_1}')
print(f'Sua última aparição é na posição {posição_final}')
