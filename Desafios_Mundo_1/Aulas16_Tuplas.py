lanche = ('Hambúrguer', 'Pizza', 'Batata Frita', 'Pudim')

print(lanche[-1:]) # começa a contagem da direita para a esquerda

for comida in lanche:
    print(f'{comida}')

for cont in range(0, len(lanche)):# se precisar da posição
    print(f'{lanche[cont]} na posição {cont}')

for posição, comida in enumerate(lanche):# se precisar da posição
    print(f'{comida} na poisção {posição}')

print(sorted(lanche)) # coloca os elementos da tupla em ordem alfabética

a = (1, 4, 7)
b = (2, 7, 5, 1)
c = a + b # uni as tuplas sem colocar em ordem e sem tirar valores e [a+b != b+a]
print(sorted(c)) # coloca em ordem
print(len(c)) # quantos itens tem a tupla
print(c.count(5)) # quantas vezes determinado elemento aparece na tupla
print(c.index(4)) # indica a posição de determinado elemento dentro da tupla, sendo apenas a 1ª
print(c.index(2, 2)) # o mesmo do anteiror apontando a partir de qual posição deve mostra a poisição do elemto procurado

del(c) # deleta um tupla, não um elemtno da tupla

