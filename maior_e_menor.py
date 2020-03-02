#coding: utf-8

n = int(input("Digite o valor de N: "))
i = 0
maior = 0
menor = 0

while (i < n):
  numero = float(input("Digite um número real: "))

  if (i == 0 or numero > maior):
    maior = numero

  if (i == 0 or numero < menor):
    menor = numero

  i += 1

print("O menor número é {}").format(menor)
print("O maior número é {}").format(maior)
