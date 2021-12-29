# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

numero = int(input('Digite um número: '))
print(f'A TABUADA DE {numero} É:')
for c in range(1, 11):
    print(f'{numero} x  {c:2} = {numero * c:2}')
    