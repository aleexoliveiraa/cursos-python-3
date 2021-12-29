'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros'''

print(f'{" LOJAS OLIVEIRA ":=^40}') 
print('AMBIENTE DE CHECKOUT')
preço = float(input('Informe o preço da mercadoria: R$'))
print(''' FORMAS DE PAGAMENTO: 
[ 1 ] à vista no dinheiro / Pix (10% de DESCONTO)
[ 2 ] à vista no cartão de crédito(5% DE DESCONTO)
[ 3 ] em até 2x no cartão
[ 4 ] em 3x ou mais no cartão (com 20% DE JUROS)''')        
pagamento = int(input('Informe a forma de pagamento: '))
if pagamento == 1:
    print(f'Pagamento em dinheiro/Pix: Total R${preço * 0.9:.2f}.')
elif pagamento == 2:
    print(f'Pagamento em 1x no cartão: Total R${preço * 0.95:.2f}')
elif pagamento == 3:
    print(f'Pagamento em 2x de R${preço / 2:.2f} no cartão: Total R${preço:.2f}')
elif pagamento == 4:
    parcelas = int(input('Número de parcelas: '))
    print(f'Pagamento em {parcelas}x de R${(preço * 1.2) / parcelas :.2f} no cartão: Total R${preço*1.2:.2f}')
else:
    print('OPÇÃO INVÁLIDA. Tente novamente!')