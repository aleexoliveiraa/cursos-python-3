'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais 
velho e quantas mulheres têm menos de 20 anos.'''

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulhermenor = 0
for dados in range(1, 5):
    print(f'----- {dados}ª Pessoa -----')
    nome = str(input(f'Nome: ')).strip().title()
    idade = int(input(f'Idade: '))
    gênero = str(input('Gênero [M/F]: '))
    somaidade += idade
    if dados == 1 and gênero in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if gênero in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if gênero in 'Ff' and idade < 20:
        mulhermenor += 1

mediaidade = somaidade / dados
print(f'A média de idade do grupo é de {mediaidade:.0f} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos e seu nome é {nomevelho}.')
print(f'Ao todo são {mulhermenor} mulheres menores de 20 anos.')