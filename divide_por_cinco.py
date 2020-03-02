#coding: utf-8

minimo = int(input("Digite o valor mínimo: "))
maximo = int(input("Digite o valor máximo: "))

if (minimo > maximo):
  print("O valor mínimo deve ser menor do que o valor máximo")
else:
  i = minimo
  while(i <= maximo):
    if (i % 5 == 0):
      print("{} é divisível por 5").format(i)
    i += 1
