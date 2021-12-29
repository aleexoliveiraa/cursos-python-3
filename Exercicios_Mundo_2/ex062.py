# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print('GERADOR DE PA')
print('=-=' * 10)
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont < total:
        print(f'{termo} → ', end='')
        termo += razão
        cont += 1
    print('Pausa...')
    mais = int(input('Deseja mostrar mais quantos termo? '))
print(f'PA finalizada com {total} termos.')