'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    op = str(input('Quer continuar? [S/N] ')).lower()
    if op == 'n':
        break
print('-=' * 30)
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores em orde descrescente são: {lista.sort(reverse=True)}')
if 5 in lista:
    print('O valor 5 foi encontrado na lista!')
else:
    print('O valor 5 não foi encontrado na lista')