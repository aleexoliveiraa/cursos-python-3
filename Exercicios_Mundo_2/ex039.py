from datetime import date
'''Faça um programa que leia o ano de nascimento de um jovem e informe, 
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

print('\033[32m=\033[m' * 25)
print('''Informe seu gênero:
\033[1m[ 1 ] Masculino
[ 2 ] Feminino\033[m''')
print('\033[32m=\033[m' * 25)
gênero = int(input('Informe a opção: '))
if gênero == 2:
    print('Mulheres não são obrigadas ao alistamento militar!')
else:
    ano = int(input('Informe seu ano de nascimento: '))
    idade = date.today().year - ano
    print(f'Quem nasceu em {ano} tem {idade} anos em {date.today().year}.')
    if idade < 18:
        print(f'Ainda faltam {18 - idade} anos para o seu alistamento!')
        print(f'Se alistamento será em {ano + 18}.')
    elif idade == 18:
        print(f'Você tem que se alistar IMEDIATAMENTE!')
    elif idade > 18:
        print(f'Você deveria ter se alistado à {idade - 18} anos')
        print(f'Seu alistamento foi em {ano + 18}.')
