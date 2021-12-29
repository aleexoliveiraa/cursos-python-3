# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
# desconsiderando os espaços. Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
união = ''.join(palavra)
inverso = ''
for letra in range (len(união) - 1, - 1, - 1):
    inverso += união[letra]
print(f'O inverso de {união} é {inverso}.')
if inverso == união:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada não é um palímdromo.')