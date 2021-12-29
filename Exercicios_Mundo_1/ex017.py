from math import hypot
cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjascente = float(input('Comprimento do cateto adjascente: '))
print(f'A hipotenusa é de {hypot(cateto_oposto , cateto_adjascente):.2f}')
