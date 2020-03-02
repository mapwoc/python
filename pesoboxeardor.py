#marcos dias
#verifica qual categoria o peso de um boxeador se encontra

peso = float(input("Digite o peso do boxeador: "))

if (peso < 65):
  print("Categoria Pena")
elif (peso >= 65 and peso < 72):
  print("Categoria Leve")
elif (peso >= 72 and peso < 79):
  print("Categoria Ligeiro")
elif (peso >= 79 and peso < 86):
  print("Categoria Meio Médio")
elif (peso >= 86 and peso < 93):
  print("Categoria Médio")
elif (peso >= 93 and peso < 100):
  print("Categoria Meio Pesado")
elif (peso >= 100):
  print("Categoria Pesado")
