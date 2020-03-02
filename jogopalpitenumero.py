'''
Gera um numero randomico de 1 a 9 e pede um palpite como entrada e verifica se o palpita esta correto

'''

# Solução
import random

guess_log = []
generated_number = random.randint(1, 9)
while True:
    # Input 
    input_string = input('Dê um palpite entre 1 e 9 ou digite exit para sair do jogo ')
    if input_string.lower() == 'exit':
        print('Até mais!')
        break
    # Check the input value
    try:
        guess_number = int(input_string)
        if guess_number not in range(1, 10):
            print('Numero não pode ser aceito.')
            continue
    except:
        print('Erro .')
        continue
    # Compare
    guess_log.append(guess_number)
    if guess_number != generated_number:
        print('Seu palpite é muito alto!' if guess_number > generated_number else 'Seu palpite é muito baixo!')
    else:
        print('Correto! Seu {} Palpite.\n{}'.format(len(guess_log), guess_log))
        # Reset
        guess_log = []
        generated_number = random.randint(1, 9)
