# Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle

nome1 = str(input('Digite o aluno 1: '))
nome2 = str(input('Digite o aluno 2: '))
nome3 = str(input('Digite o aluno 3: '))
nome4 = str(input('Digite o aluno 4: '))

listaAlunos = [nome1, nome2, nome3, nome4]

shuffle(listaAlunos)

print('A ordem de apresentação será:\n{} '.format(listaAlunos))
