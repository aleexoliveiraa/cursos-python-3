from datetime import date
'''A Confederação Nacional de Natação precisa de um programa que leia 
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER'''

print('-=-' * 20)
print('\033[1;33mCONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[m')
print('-=-' * 20)
ano = int(input('Informe o ano de nascimento do participante: '))
idade = date.today().year - ano
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classíficação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
elif idade > 25:
    print('Classificação: MASTER')
    