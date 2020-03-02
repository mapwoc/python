'''
Lista de palavras

Verifica se palavra ou frase pode ser um palimdromo

'''
#Palindromo é uma palavra ou frase que pode ser lida de ambos os lados de forma igual, ex ana, luz azul
# dá erro em palavras separada por espaço
input_string = input("Insira uma string:")
print("String é um palindromo" if input_string[::-1] == input_string else "A string não é um palindromo")
