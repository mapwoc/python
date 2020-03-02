#Exercício Python 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
num = int(input('Digite um numero inteiro: '))

print('O sucessor e o antecessor do numero {} são respectivamente {} e {}'.format(num, num+1, num-1))