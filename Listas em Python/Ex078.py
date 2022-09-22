'''Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. '''

valores = []
menor = 0
maior = 0

for i in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {i}: ')))
    if i == 0:
        maior = menor = valores[i]
    else:
        if valores[i] > maior:
            maior = valores[i]
        if valores[i] < menor:
            menor = valores[i]

print('-=' * 30)
print(f'Você digitou os valores {valores}')
print(f"O maior valor digitado foi o {maior} na posição ", end='')

for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f"O menor valor digitado foi o {menor} na posição ", end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
print()


