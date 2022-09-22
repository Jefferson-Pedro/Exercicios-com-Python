'''Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

with open("tabela.txt", "r", encoding = "UTF-8") as tabela:
    linha = list(tabela.read().split(','))
novaTupla = tuple(linha)

print('Lista de tumes do Brasileirão: ', novaTupla)
print('-='*20)
print('Os primeiros 5 times são: ', novaTupla[0:5])
print('-='*20)
print('Os 4 ultimos são: ', novaTupla[-4::1])
print('-='*20)
print('Times em ordem alfabéticas são: ', sorted(novaTupla))
print('-='*20)
print('Posição do Mengão: {}º posição'.format(novaTupla.index('Flamengo')))