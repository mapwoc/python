#marcos dias
#escreve um numero inteiro e informa se é positivo ou negativo

numero = int(input("Digite um número inteiro: "))

if (numero > 0):
  print("{} é positivo").format(numero)
elif (numero < 0):
  print("{} é negativo").format(numero)
else:
  print("Você digitou zero")
