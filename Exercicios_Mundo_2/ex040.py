'''Crie um programa que leia duas notas de um aluno e calcule sua média, 
mostrando uma mensagem no final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO'''

n1 = float(input('PRIMEIRA NOTA: '))
n2 = float(input('SEGUNDA NOTA: '))
média = (n1 + n2) / 2
print(f'Com as notas {n1:.1f} e {n2:.1f}, a média do aluno é {média:.1f}.')
if média >= 7.0:
    print(f'\033[1;32mO aluno foi APROVADO!\033[m')
elif média >= 5.0:
    print(f'\033[1;33mO aluno está em RECUPERAÇÃO!\033[m')
elif média < 5.0:
    print(f'\033[1;31mO aluno foi REPROVADO!\033[m')
