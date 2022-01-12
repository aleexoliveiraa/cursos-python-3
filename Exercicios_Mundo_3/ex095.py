'''Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

jogador = {}
partidas = []
time = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Número de partidas jogadas que {jogador["nome"]} fez: '))
    partidas.clear()
    for p in range(0, total):
        partidas.append(int(input(f'  Quantidade de gols da {p + 1}ª: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if continuar == 'N':
        break
print('--' * 30)
print('Cod ', end='')
for indice in jogador.keys():
    print(f'{indice.title():<15}', end='')
print()
print('--' * 30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15} ', end='')
    print()
print('--' * 30)
while True:
    busca = int(input('Mostrar detalhes de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}! ')
    else:
        print(f' -- LEVATAMENTO DO JOGADOR {time[busca]["nome"].upper()}: ')
        for indice, gol in enumerate(time[busca]["gols"]):
            print(f'    - Na {indice + 1}ª partida fez {gol} gols.')
    print('--' * 30)
print('>>>FINALIZANDO! VOLTE SEMPRE<<<<')