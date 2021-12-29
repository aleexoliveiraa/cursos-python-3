lanche = ('Hambúrguer', 'Pizza', 'Batata Frita', 'Pudim')

for comida in lanche:
    print(f'{comida}')

for cont in range(0, len(lanche)):# se precisar da posição
    print(f'{lanche[cont]} na posição {cont}')

for posição, comida in enumerate(lanche):# se precisar da posição
    print(f'{comida} na poisção {posição}')
