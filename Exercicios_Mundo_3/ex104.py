'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt(‘Digite um n: ‘)'''

def leiaInt(n):
    while True:
        if n.isnumeric():
            break
        elif n.:
            return f'\033[32mERRO! NENHUM NÚMERO FOI DIGITADO.\033[m'
            n = input('Digite um número: ')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')