'''Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma
contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado
(entre 0 e 20) e mostrá-lo por extenso.'''

tuplas = (
"zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze",
"quartorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

escolha = int(input('Digite um valor entre 0 e 20: '))
while(True):
    if (escolha < 0) or (escolha > 20):
        escolha = int(input('Tente novamente.Digite um valor entre 0 e 20: '))
    else:
       print(f'você digitou o valor: {tuplas[escolha]}')
    break
print('Fim do programa')