km = float(input('Digite a quilometragem pecorrida: '))
dias = float(input('Digite a quantidade de dias alugados: '))
preço_km = km * 0.15
preço_dias = dias * 60
print(f'O preço final do aluguel do carro será R${preço_km + preço_dias :.2f}.')