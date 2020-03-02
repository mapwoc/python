'''
Lista sobrepostas 

Tendo as duas listas abaixo 

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
faça um programa que retorne 1 elemento de cada lista,  apenas os elementos
repetitivos
'''
import random
# Solution
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = [int(10 * random.random()) for i in range(20)] #cria uma lista ramdomica de n int com 20 elementos
b = [int(10 * random.random()) for i in range(15)] #cria uma lista ramdomica de n int com 15 elementos
print("Lista 1: ", a)
##print("Lista 2: ", b)
print("Sobrepoem: ", list(set(a).intersection(b))) #gera lista de num sopbrepostos, que existe me ambas listas
