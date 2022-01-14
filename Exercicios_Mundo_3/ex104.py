'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt(‘Digite um n: ‘)'''

def leiaInt(msg):
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            int(n)
            ok = True
        else:
            print(f'\033[32mERRO! NENHUM NÚMERO FOI DIGITADO.\033[m')
        if ok:
            break


num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}')
