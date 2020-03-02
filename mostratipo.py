#Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
algo = input('Digite algo: ')

print('Tipo: {}'.format(type(algo)))
print('Só espaços: {}'.format(algo.isspace()))
print('Númerico: {}'.format(algo.isnumeric()))
print('Alfabetico: {}'.format(algo.isalpha()))
print('Alfanumérico: {}'.format(algo.isalnum()))
print('Palavra escritas em maiúsculo: {}'.format(algo.isupper()))
print('Letras escritas em minúsculo: {}'.format(algo.islower()))
print('Capitalizada: {}'.format(algo.istitle()))