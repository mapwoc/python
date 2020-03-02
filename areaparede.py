#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))

area = altura * largura
qtdLitrosTinta = area/2

print('A área da parede e a quantidade de tinta para ser pintada são respectivamente {} metros quadrados e {} litros'.format(area, qtdLitrosTinta))