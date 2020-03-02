#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Digite a quantidade de de dias que o carro foi alugado: '))
qtdKm = float(input('Digite a quantidade de km pecorrida do carro alugado: '))

preco = qtdKm * 0.15 + dias * 60;

print('O preco a se pagar por {:.2f} km pecorridos e {} dias alugados é: {:.2f}'.format(qtdKm, dias, preco))