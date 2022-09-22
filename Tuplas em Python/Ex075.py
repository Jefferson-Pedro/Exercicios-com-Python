'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

num = (int(input('Digite um numero: ')),
        int(input('Digite outro numero: ')),
        int(input('Digite mais um numero: ')),
        int(input('Digite o ultimo numero: ')))
print(f'Você inseriu os valores {num}')
if 9 in num:
    print('O valor 9 apareceu {} vezes'.format(num.count(9)))
else:
    print('O valor 9 não foi digitado!')
if 3 in num:
    print('O valor 3 apareceu {} vezes, na posição {}'.format(num.count(3), num.index(3)))
else:
    print('O número 3 não foi digitado!')
print('Os valores pares digitados foram ', end='')
for c in num:
    if c % 2 == 0:
        print(c, end=' ')





