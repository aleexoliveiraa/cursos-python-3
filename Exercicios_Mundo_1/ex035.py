# Desenvolva um programa que leia o comprimento de 
# três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('-=-' * 20)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-' * 20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    verdadeiro = '\033[1;32mPODEM\033[m'
else:
    verdadeiro = '\033[1;31mNÃO PODEM\033[m'
print(f'Os segmentos informados {verdadeiro} FORMAR um triàngulo!')
