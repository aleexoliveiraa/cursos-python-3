'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela.'''

ficha = {}
ficha['nome'] = str(input('Nome: '))
ficha['média'] = float(input('Média: '))
if ficha['média'] >= 7:
    ficha['situação'] = 'APROVADO'
elif 5 <= ficha['média'] < 7:
    ficha['situação'] = 'RECUPERAÇÃO'
else:
    ficha['situação'] = 'REPROVADO'
print('-=' * 30)
for chave, valor in ficha.items():
    print(f'    - {chave} é igual {valor}.')
