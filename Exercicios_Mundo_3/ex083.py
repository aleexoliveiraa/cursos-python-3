'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo 
deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

expressão = str(input('Digite sua expressão: '))
validação = []
for parêntese in expressão:
    if parêntese == '(':
        validação.append('(')
    elif parêntese == ')':
        if len(validação) > 0:
            validação.pop
        else:
            validação.append(')')
            break
if len(validação) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão não é válida')