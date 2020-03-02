#coding: utf-8

n = int(input("Digite o valor de N: "))
i = 0
iniciado = False
maior = 0
menor = 0

while (i < n):
  numero = float(input("Digite um número real: "))

  if (iniciado == False and numero > 0):
    iniciado = True
    maior = numero
    menor = numero

  if (iniciado == False or numero > maior):
    maior = numero

  if (iniciado == False or numero < menor):
    menor = numero

  i += 1

print("O menor número é {}").format(menor)
print("O maior número é {}").format(maior)
