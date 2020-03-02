#Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
real= float(input('Digite quanto dinhero voce tem em reais: '))

dolar = real / 3.27;

print('Com {:.2f} reais você pode comprar {:.2f} doláres'.format(real, dolar))