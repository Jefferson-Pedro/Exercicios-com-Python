'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários
valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro,
ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. '''

lista = []
valor = 0
op = 'S'

while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('valor adicionado com sucesso...')
        op = str(input('Deseja continuar? [S/N] ').lower())
    else:
        print('valor duplicado! Não vou adicionar...')
        op = str(input('Deseja continuar? [S/N] ').lower())
    if op == 'n':
        lista.sort()
        print(f'Você digitou os valores {lista}')
        break




#  else:  lista.append(int(input('Valor duplicado! Não vou adicionar...')))

'''   
        
        op = input('Deseja continuar? [S/N]').lower()'''