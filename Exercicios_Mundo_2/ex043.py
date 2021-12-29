'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida'''

print('-' * 10 + ' CALCULADORA DE IMC ' + '-' * 10)
peso = float(input('Infome seu peso em Kg: '))
alt = float(input('Infomre sua altura em metros: '))
imc = peso / (alt**2)
print(f'O IMC DESSA PESSOA É IGAL A {imc:.1f}.')
if imc < 18.5:
    print('Você se encontra ABAIXO DO PESO normal!')
elif 18.5 <= imc < 25:
    print('PARABÉNS! Você se encontra no PESO IDEAL.')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO, fique ATENTO!')
elif 30 <= imc < 40:
    print('Você esta com OBESIDADE, CUIDADO!')
elif imc <= 40:
    print('Você se encontra em OBESIDADE MÓRBIDA, necessita de cuidados URGENTES!')
