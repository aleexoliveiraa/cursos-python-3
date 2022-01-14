cor = ('\033[m',        # 0 - sem cor
       '\033[0;30;41m', # 1 - vermelho
       '\033[0;30;42m', # 2 - verde
       '\033[0;30;43m', # 3 - amarelo
       '\033[0;30;44m', # 4 - azul
       '\033[0;30;45m', # 5 - roxo
       '\033[7;30m'     # 6 - branco
       )


def ajuda(comando):
    print(f'Acessando o manual do comando \'{comando}\'', 6)
    print(cor[6], end='')
    help(comando)
    print(cor[0], end='')


def título(texto, cores=0):
    tamanho = len(texto) + 6
    print(cor[cores], end='')
    print('-=' * tamanho)
    print(f'   {texto}')
    print('-=' * tamanho)
    print(cor[cores], end='')


comando = ''
while True:
    título('SISTEMA DE AJUDA PYHELP', 1)
    comando = str(input('FUNÇÃO OU BIBLIOTECA > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
