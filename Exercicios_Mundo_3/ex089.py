'''Crie um programa que leia nome e duas notas de vários alunos e guarde 
tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um 
e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
lista_final = []
while True:
    nome = str(input('Aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2)/2
    lista_final.append([nome, [nota1, nota2], média])
    continuar = str(input('Deseja cadastrar mais alunos: [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
print('-=' * 35)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 25)
for indice, aluno in enumerate(lista_final):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    print('-' * 35)
    notas = int(input('Deseja ver as notas de qual aluno? (999 interrompe): '))
    if notas == 999:
        print('FINALIZANDO...')
        break
    if notas <= len(lista_final) - 1:
        print(f'As notas de {lista_final[notas][0]} são {lista_final[notas][1]}')
        