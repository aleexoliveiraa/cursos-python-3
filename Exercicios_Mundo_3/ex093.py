'''Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''


dados = {}
dados['jogador'] = str(input('Nome do jogador: '))
partidas = int(input(f'Número de partidas jogadas que {dados["jogador"]} fez: '))
total = 0
gols = []
print('-=' * 30)
print("GOLS POR PARTIDA")
for partida in range(0, partidas):
    gols.append(int(input(f'  Quantidade de gols da {partida + 1}ª: ')))
dados['gols'] = gols[:]
dados['total'] = sum(gols)
print('-=' * 30)
print(dados)
print('-=' * 30)
for chave, valor in dados.items():
    print(f'O campo {chave} tem o valor {valor}')
print('-=' * 30)
print(f'O jogador {dados["jogador"]} fez {len(dados["gols"])} partidas.')
for chave, valor in enumerate(gols):
    print(f'    Na {chave + 1}ª partida, fez {valor} gols')
print(f'O total de gols foram de {dados["total"]}')
