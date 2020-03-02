#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite o salario do funcionario em reais: '))

novoSalario = salario + (salario * 0.15)

print('O salário que antes era {} reais com 15% de aumento equivale a {} reais'.format(salario, novoSalario))