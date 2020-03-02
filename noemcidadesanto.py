#Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cidade = str(input('Digite um nome de uma cidade: ')).strip()
n = cidade.upper().find('SANTO')

print(n == 0)