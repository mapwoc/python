#Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc  

num = float(input('Digite um numero real: '))
numInt = trunc(num)

print('A parte inteira do numero {:.2f} é igual a {}'.format(num, numInt))
