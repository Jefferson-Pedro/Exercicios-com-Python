'''Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar
em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor
e o maior valor que estão na tupla.'''
import random

numero = random.sample(range(10),5)
valorMaior = max(numero)
valorMenor = min(numero)
print('Os valores gerados foram: {}'.format(tuple(numero)))
print('O maior valor foi: ', valorMaior)
print('O menor valor foi: ', valorMenor)




