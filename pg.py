#coding: utf-8

t1 = int(input("Primeiro termo: "))
r = int(input("Razão da PG: "))
n = int(input("Quantidade de termos: "))

i = 0
valor = t1
soma = t1

while (i < n - 1):
  valor = valor * r
  soma += valor
  i += 1

print("Total da PG: {}").format(valor)
print("Soma dos termos da PG: {}").format(soma)
