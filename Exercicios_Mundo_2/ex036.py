# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('\033[1;34m--=--\033[m' * 10)
print('SIMULADOR DE FINANCIAMENTO')
print('\033[1;34m--=--\033[m' * 10)

valor = float(input('Valor da casa: R$'))
salario = float(input('Informe o seu salário: R$'))
tempo = int(input('Informe em quantos anos deseja pagar: '))
prestação = valor / float((tempo * 12))
if prestação <= (salario * 0.3):
    print(f'\033[32mAPROVADO!\033[m seu financimaneto para o valor de R${valor:.2f} a ser pago em {tempo * 12} meses com prestações de R${prestação:.2f} ')
else:
    print(f'Financimaneto \033[31mNEGADO\033[m!')