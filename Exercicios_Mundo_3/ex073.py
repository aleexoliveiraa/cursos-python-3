'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela 
do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza',
        'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
        'Atlético-GO', 'Santos', 'Ceará-SC', 'Internacional', 'São Paulo',
        'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio',
        'Bahia', 'Sport Recife', 'Chapecoense')
print('=' * 50)
print(f'Lista de times do Brasileirão 2021: {times}')
print('=' * 50)
print(f'Primeiros 5 colocados: {times[0:5]}')
print('=' * 50)
print(f'Últimos 4 colocados: {times[-4:]}')
print('=' * 50)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=' * 50)
print(f'O Chapecoense se encontra na {times.index("Chapecoense") + 1}ª posição')