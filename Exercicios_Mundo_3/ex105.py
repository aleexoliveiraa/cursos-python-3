'''Faça um programa que tenha uma função notas() que pode receber várias
notas de alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
- A menor nota
— A média da turma
– A situação (opcional) '''


def nota(*n, sit=False):
    """
    => Função apara análise das notas de um aluno
    :param n: informar as notas, sem limite para cadastro
    :param sit: opcional, retorna qqual a situação do aluno de acordo com a média
    :return: retorna uma análise detalhada das notas do aluno
    """
    r = {}
    r['total'] = len(n)
    r['máx'] = max(n)
    r['min'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'REGULAR'
        else:
            r['situação'] = 'RUIM'
    return r


resposta = nota(8, 5, 9.5, 7, sit=True)
print(resposta)
help(nota)