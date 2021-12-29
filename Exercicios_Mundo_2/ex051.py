# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão.

print('=' * 10)
print('')

termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = razão * 10 + 1
for c in range(termo, décimo, razão):
    print(c, end=' → ')
print('ACABOU')