'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.
'''
nome =  str(input('Digite seu nome completo: ')).strip()
print(f'Analisando seu nome... \nSeu nome em letras maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
nome_dividido = nome.split()
nome_sem_espaço = ''.join(nome_dividido)
print(f'Seu nome tem ao todo {len(nome_sem_espaço)} letras')
### ou: print(f'Seu nome ao todo possui {len(nome) - nome.count(' ')} letras') 

print(f'Seu primeiro nome é {nome_dividido[0]} e tem {len(nome_dividido[0])} letras')
### ou: print(f'Seu primeiro nome é {nome_dividido[0]} e tem {nome.find(' ')} letras')