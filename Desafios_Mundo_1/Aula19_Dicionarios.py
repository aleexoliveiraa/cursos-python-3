'''pessoas = {'nome': 'Alex', 'idade': 29, 'sexo': 'M'}
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos de idade.')
print(pessoas.keys()) # chaves das variáveis
print(pessoas.values()) #valores das variáveis
print(pessoas.items()) # cria uma composição de lista com tuplas, onde lista contém todos os elementos do dicionário e as tuplas as variáveis e seu valores respectivamente
for chave in pessoas.keys(): # vale para os values.
    print(chave)
for chave, valor in pessoas.items():
    print(f'{chave}: {valor}')

pessoas['nome'] = 'Fernando' #TROCA DE VALORES
del pessoas['sexo'] #deleta a variável e seu valor
pessoas['peso'] = 80.5 #adiciona uma variável e seu valor ao dicinário

###############################################################################################
brasil = []
estado1 = {'uf': 'Minas Gerais', 'sigla': 'MG'}
estado2 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]) # para acessar qualquer valor dentro da lista se matnám a sintaxe já aprendida
print(brasil[0]['sigla']) # para acessar o elemnto do dicionário usar a chave'''

#############################################################################################

estado = dict() #código para criar dicionário
brasil2 = []
for contador in range (0,3):
    estado['uf'] = str(input('Estado: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil2.append(estado.copy()) # metodo para fatiar dicionários e não sobreescrever valores na lista
for estado in brasil2:
    for chave, valor in estado.items():
        print(f'O campo {chave} tem valor {valor}')
        