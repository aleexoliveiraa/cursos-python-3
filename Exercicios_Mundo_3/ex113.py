'''Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora
a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''


def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO! Digite apenas um valor inteiro.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mERRO! O usuário decidiu abandonar o programa!\033[m')
            return 0
        else:
            return n


def leia_float(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO! Digite apenas um valor real.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mERRO! Usuário decidiu abandonar o programa.\033[m')
            return 0
        else:
            return n


n1 = leia_int('Digite um número inteiro: ')
n2 = leia_float('Digite um número Real: ')
print(f'Foi digitado o valor inteiro {n1} e o Real {n2}.')
