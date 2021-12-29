# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distância = float(input('Digite a distância em KM da viagem: '))
if distância <= 200:
    print(f'O preço da sua passagem será R${distância * 0.50:.2f}')
else:
    print(f'O preço da sua passagem será de R${distância * 0.45:.2f}.')

preço = distância * 0.50 if distância <= 200 else distância * 0.45
print(f'O preço da sua passagem será de R${preço:.2f}')
