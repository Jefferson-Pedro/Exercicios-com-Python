'''Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

expressao = []

expressao = str(input('Digite sua expressão: '))

print(f'A expressão digitada {expressao} ', end='')
if expressao.count('(') == expressao.count(')'):
    print("está correta")
else:
    print('está incorreta')


