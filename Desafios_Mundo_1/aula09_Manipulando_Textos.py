frase = 'Curos em Vídeo Python'

'''FATIAMENTO'''
print(frase[9:13:2])
'''
mostra a partir do 10° pulando de 2 em 2
[:15] indica o final a partir do 0
[15:] indica o inicio até o final
[9::3] indica o inicio até o final pulando de 3 em 3
'''

'''ANÁLISE'''
print(len(frase))
'''Indica o número de caracterres de uma string'''

print(frase.count('o'))
'''exibe o número de caracteres iguais ao informado nos parentêses
-VARIAÇÕES:
frase.count('o', 0, 13) - indica o intervalo entre os caracteres a fazer a contagem 
'''

print(frase.find('deo'))
'''indica a posição inicial onde começa o objeto procurado
Caso o valor procurado não exista no intervalo, será retornado o valor (-1)
'''

print('Curso' in frase)
'''indica se o valor procurado existe no intervalo'''

'''TRANSFORMAÇÃO'''
print(frase.replace('Python', 'Android'))
'''substitui um termo por outro dentro do intervalo'''

print(frase.upper())
'''coloca todos os caracteres em maiúsculas'''

print(frase.lower())
'''coloca todos os caracteres em minúsculas'''

print(frase.capitalize())
'''coloca o primeiro caractere do intervalo em maiúscula e todas os outros em minúsculas'''

print(frase.title())
'''coloca a primeira letra de cada palavra em maiúscula'''

frase2 = '   Aprenda Python  '

print(frase2.strip())
'''remove os espaços no início e final da string'''

print(frase2.rstrip())
'''remove os espaços do final da string'''

print(frase2.lstrip())
'''remove os espaços do ínicio da string'''

'''DIVISÃO'''
dividido = frase.split()
print(dividido)
'''divide a string nos espaços'''

print(dividido[0])
'''mostra o primeiro item da lista'''

'''JUNÇÃO'''
print('-'.join(dividido))
'''junta as string com um hífen ou espaço caso queira'''











'''DICA'''
print("""O Lorem Ipsum é um texto modelo da indústria tipográfica e de impressão. 
O Lorem Ipsum tem vindo a ser o texto padrão usado por estas indústrias desde o 
ano de 1500, quando uma misturou os caracteres de um texto para criar um espécime 
de livro. Este texto não só sobreviveu 5 séculos, mas também o salto para a tipografia 
electrónica, mantendo-se essencialmente inalterada. Foi popularizada nos anos 60 com a 
disponibilização das folhas de Letraset, que continham passagens com Lorem Ipsum, e mais 
recentemente com os programas de publicação como o Aldus 
PageMaker que incluem versões do Lorem Ipsum.""")

