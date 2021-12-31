# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

extenso = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'catorze',
           'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')
while True:
    posicao = int(input('Digite um número de 0 a 20: '))
    while posicao < 0 or posicao > 21:
        posicao = int(input('Valor incorreto. Digite novamente: '))
    print(f'Você digitou o número {extenso[posicao]}.')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'S':
        posicao = int(input('Digite um número de 0 a 20: '))
    elif continuar == 'N':
        break
