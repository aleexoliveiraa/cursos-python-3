# o while serve pricipalemte para quando não se sabe o limite da repetição do laço
# EXEMPLO 1:
c = 1 #o contador começa com...
while c < 10: # condição para continuar a reteição do laço
    print(c)
    c += 1 # condição para somar e não rodar o laço infinitamente
print('ACABOU')

# EXEMPLO 2:
while c != 0: #flag: condição de parada
    c = int(input('Digite um valor: '))
print('FIM')

# EXEMPLO 3:
r = 'S'
while r == 'S':
    n = int(input('Digite um valor:'))
    r = str(input('Deseja continuar? [S/N] ')).upper()
print('Acabou/!')

# EXEMPLO 4:
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} número pares e {impar} números ímpares.')