# Faça um programa que leia o nome completo de uma pessoa, 
# mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).title().strip().split()
print(f'Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}.')
print(f'E o seu último nome é {nome[len(nome) - 1]}')
print(f'Último nome: {nome[-1]}')
print(f'Seja bem-vindo {nome[0]} {nome[-1]}!')
