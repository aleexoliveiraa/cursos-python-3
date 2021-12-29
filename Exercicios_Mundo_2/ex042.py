'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar 
que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes'''

print('-=-' * 20)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-' * 20)

r1 = float(input('PRIMEIRO SEGMENTO:'))
r2 = float(input('SEGUNDOSEGMENTO: '))
r3 = float(input('TERCEIRO SEGMENTO: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    if r1 == r2 == r3:
          categoria = 'EQUILÁTERO'
    elif r1 != r2 != r3 != r1:
        categoria = 'ESCALENO'
    else:
        categoria = 'ISÓCELES'
    print('Os segmentos informados \033[1mPODEM\033[m FORMAR um triângulo {categoria}!')
else:
    print('Os segmentos informados \033[1;31mNÃO PODEM\033[m FORMAR um triângulo.')