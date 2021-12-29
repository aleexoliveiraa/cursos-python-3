for c in range(0, 10): # o final é sempre desconsiderado
    print(c)

for c in range(0, 10, 2): # 1= inicio 2= final -1 3= intervalo a ser pulado
    print(c)

for c in range(0, 3):
    print('oi')
print('FIM')

for c in range(6, 0, -1): #para contar pra trás
    print(c)

n = int(input('Digite um número: '))
for c in range(0, n + 1):
    print(c)

i = int(input('Início: '))
f = int(input('Final: '))
p = int(input('Passo:'))
for c in range(i, f+1, p):
    print(c)

s = 0
for c in range(0, 4):
    n = int(input('Digite um número: '))
    s += n #soma
print(f'O somatório é igual a {s}')