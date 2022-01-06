teste = list()
teste.append('Alex')
teste.append(29)
galera = list()
galera.append(teste[:]) # o comando [:] faz uma cópia desvinculada da lista, podendo assim ser mudados os elemntos posteriormente e não
teste[0] = 'Maria'
teste[1] = 40
galera.append(teste)
print(galera)

galera_2 = [['Alex', 29], ['Felipe', 25], ['Maria', 55], ['Ana', 18]]
print(galera_2[1][0]) # A primeira [] referece à lista superior e a segunda ao elemento dentro da lista inferior.
for p in galera_2:
    print(f'{p[0]} tem {p[1]} anos de idade.')

galera_3 = []
dado = []
totalmaior = totalmenor = 0
for p in range(0, 3):
    dado.append(str(input('Nome: '))) #dados para cada pessoa
    dado.append(int(input('Idade: ')))
    galera_3.append(dado[:]) #cópia para a lista galera
    dado.clear() #apago os dados a cada vez que fizer o laço

for p in galera_3:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totalmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totalmenor += 1
print(f'Temos {totalmaior} maiores de idade e {totalmenor} de menor.')