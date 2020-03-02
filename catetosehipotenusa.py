#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import hypot

catOp = float(input('Digite o cateto oposto do triangulo retângulo: '))
catAd = float(input('Digite o cateto adjacente do triangulo retângulo: '))

hp = hypot(catOp, catAd)

print('A hipotenusa para cateto oposto {:.2f} e cateto adjacente {:.2f} é igual a {:.2f}'.format(catOp, catAd, hp))