#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
num = int(input('Digite um numero: '))

dobro = num*2;
triplo = num*3
raizquadrada = num**(1/2)

print('O dobro, triplo e raiz quadrada do numero {} são respectivamente {}, {} e {:.2f}'.format(num, dobro, triplo, raizquadrada))