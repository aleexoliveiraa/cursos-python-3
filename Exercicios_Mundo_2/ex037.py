# Escreva um programa em Python que leia um número inteiro qualquer 
# e peça para o usuário escolher qual será a base de conversão: 
# 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número inteiro:'))
print('''Informe para qual base você deseja converter:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
print('-' * 20)
opção = int(input('Sua opção:'))
if opção == 1:
    print(f'{num} convertido em BINÁRIO é {bin(num)[2:]}') # 0b equivale a binário em python
elif opção == 2:
    print(f'{num} convertido em OCTAL é {oct(num)[2:]}') # 0o equivale a octal para o python
elif opção == 3:
    print(f'{num} convertido em HEXADECIMAL é {hex(num)[2:]}') # 0x equivale a hexadecimal para python
else:
    print('\033[32mOpção INVÁLIDA! Informe 1,2 ou 3!\033[m')