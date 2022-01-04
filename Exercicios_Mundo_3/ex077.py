'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

palavras = ('Tribo', 'Tijolo', 'Radiotransmissor', 'Local',
            'Lesma', 'Eixo', 'Uniforme', 'Magia', 'Desviar', 'Gancho')
for n in palavras:
    print(f'\nNa palavra {n.upper()} temos as vogais ', end='')
    for letra in n:
        if letra.lower() in 'aeiou':
            print(f'{letra.lower()}', end=' ')