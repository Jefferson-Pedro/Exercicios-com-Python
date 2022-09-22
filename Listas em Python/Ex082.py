'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

lista  = []
listaP = []
listaI = []
while True:
    lista.append(int(input('Digite um número: ')))
    op = str(input('Deseja continuar? [S/N] ')).lower()
    if op == 'n':
        break
for c in lista:
   if c % 2 == 0:
      listaP.append(c)
   else:
      listaI.append(c)

print(f'A lista completa é {lista}')
print(f'A lista de pares é {listaP}')
print(f'A lista de impares é {listaI}')