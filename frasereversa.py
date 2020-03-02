'''
Pega uma frase e inverte a sequencia das palavras

'''

def reverse_word(string): #Define o embaralhamento de plavras
    return ' '.join(string.split(' ')[::-1]) # a string é dividida e mudada
    
print(reverse_word(input('Escreva uma Frase:'))) # inicia o input da frase e faz a mudança
