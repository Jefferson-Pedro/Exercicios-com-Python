'''Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
 Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

tupla=('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
       'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')


for cont in tupla:
    print(f'\nNa palavra {cont} temos ', end='')
    for letra in cont:
       if letra.lower() in 'aeiou':
           print(letra.lower(), end=' ')
