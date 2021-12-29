# Condições: if e else
'''
nome = str(input('Digite seu nome: ')).title()
if nome == 'Alex':
    print(f'Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia, {nome}!')
'''

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n = (n1 + n2) / 2
print(f'Sua média foi {n:.1f}')
if n >= 6.0:
    print('Sua média foi boa, Parabéns!')
else:
    print('Sua média foi ruim, ESTUDE MAIS!')

print('PARABÉNS!' if n >= 6.0 else 'ESTUDE MAIS!')
