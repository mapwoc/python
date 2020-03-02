#marcos dias
# Escreve um numero inteiro e fala se é par ou impar

numero = int(input("Digite um número inteiro: "))

if (numero % 2 == 0):
  print("{} é par.").format(numero)
else:
  print("{} é impar.").format(numero)
