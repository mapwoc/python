#Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes na frase'.format(frase.upper().count('A')))
print('O primeiro A esta na posicao {} e ultimo na {}'.format(frase.upper().find('A')+1, frase.upper().rfind('A')+1))


