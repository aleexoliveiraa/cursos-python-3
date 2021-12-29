# Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
hoje = date.today().year
maior = 0
menor = 0
for pessoas in range(1, 8):
    ano = int(input(f'Em que ano a {pessoas}ª nasceu? '))
    if hoje - ano >= 21:
        maior += 1
    else:
        menor += 1
print(f'\nAo todo tivemos {maior} pessoas de maior.')
print(f'E também tivemos {menor} pessoas menores de idade.')