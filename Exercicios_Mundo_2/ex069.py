"""Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos."""

maior = homem = mulheresdemenor = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulheresdemenor += 1
    novo = ' '
    while novo not in 'SN':
        novo = str(input('Deseja cadastrar mais dados? [S/N]: ')).strip().upper()[0]
    if novo == 'N':
        break
    print('-=' * 30)


print(f'Foram cadastradas {maior} pessoas com mais de 18 anos, {homem} homens e {mulheresdemenor} mulheres com menos de 20 anos.')
