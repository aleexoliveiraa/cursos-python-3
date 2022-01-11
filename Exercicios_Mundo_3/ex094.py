'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os
dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

dados = dict()
geral = list()
soma = media = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Digite o nome: '))
    dados['idade'] = int(input('Digite a idade: '))
    soma += dados['idade']
    sexo = str(input('Digite o sexo: [M/F] ')).strip().upper()[0]
    if sexo not in 'MF':
        while sexo not in 'MF':
            sexo = str(input('ERRO! Digite apenas M ou F: ')).strip().upper()[0]
    dados['sexo'] = sexo
    geral.append(dados.copy())
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar not in 'SN':
        while continuar not in 'SN':
            continuar = str(input('ERRO! Digite apenas S ou N: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(geral)
print('-=' * 30)
print(f'Foram cadastradas {len(geral)} pessoas ao total.')
media = soma / len(geral)
print(f'A média de idades foi de {media:5.2f} anos.')
print(f'As mulheres cadastradas foram: ', end='')
for pessoas in geral:
    if pessoas['sexo'] == 'F':
        print(f'{pessoas["nome"]}', end=' ' )
print()
print('Lista de pessoas acima da média: ')
for pessoa in geral:
    if pessoa['idade'] >= media:
        print('     ', end='')
        for k, v in pessoa.items():
            print(f'{k} = {v}', end='')
            print()
print('>>>FINALIZANDO<<<')


