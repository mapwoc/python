#Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Digite o preco de um produto: '))

precoDesconto = preco - preco * 0.05

print('O produto que custava {:.2f} com 5% de desconto vale {:.2f}'.format(preco, precoDesconto))