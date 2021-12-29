# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, 
# calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Informe seu salário atual: R$'))
if salario <= 1250:
    novo = salario * 1.15
else: 
    novo = salario * 1.10
print(f'Seu novo salário é de \033[32mR${novo:.2f}\033[m')
