# Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Digite a velocidade atual do carro: '))
if velocidade > 80:
    print(f'MULTADO! Sua velocidade excedeu o limite da via de 80km/h. Você pagará uma multa de R${(velocidade - 80)*7:.2f}!')
print('Tenha um bom dia. Dirija com SEGURANÇA!')