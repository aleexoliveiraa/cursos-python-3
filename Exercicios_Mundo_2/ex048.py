# Faça um programa que calcule a soma entre todos os números que são múltiplos de três 
# e que se encontram no intervalo de 1 até 500.

soma = 0
cont = 0
for numero in range(1, 501, 2):
    if numero % 3 == 0:
        soma += numero
        cont += 1
print(f'A soma de todos dos {cont} números ímpares múltiplos de 3 no intervalo é {soma}!')
