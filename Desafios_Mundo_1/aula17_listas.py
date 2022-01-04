lista = [1, 5, 2, 9]
print(lista)
lista[2] = 3 #troca o valor
print(lista)
lista.append(6) #adciona um valor ao final da lista
print(lista)
lista.insert(3, 8) #insere um valor na posição informada
print(lista)
lista.sort() #coloca em ordem crescente
print(lista)
lista.sort(reverse=True) #coloca em ordem decrescente
print(lista)
lista.pop() #remove o último elemnto da lista
print(lista)
lista.remove(3) #remove a primeira ocorrência do elemento informado
print(f'Essa lista tem {len(lista)} elementos.') #informa a quantidade de elementos

valor = []
valor.append(4)
valor.append(2)
valor.append(9)
valor.append(3)

'''for cont in range(1, 5):
    valor.append(int(input('Digite um valor: ')))'''

for c, n in enumerate(valor):
    print(f'Na posição {c} encontrei o valor {n}')

a = [2,5,3,9]
b = a [:] #faz uma cópia da lista
b[2] = 7
print(a)
print(b)