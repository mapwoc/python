#Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
valorMetros = float(input('Digite um valor em metros: '))

valorCentimetros = valorMetros * 100;
valorMilimetros = valorMetros * 1000;

print('{} metros equivale em centimetros e milímetros respectivamente {} e {}'.format(valorMetros, valorCentimetros, valorMilimetros))