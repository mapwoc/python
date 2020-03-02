'''
marcos dias
calcula a idade da pessoa no ano atual
'''


import datetime

while True:
    name = input("Escreva Seu Nome：") #pergunta o nome
    age = int(input("Digite Sua idade：")) # pergunta idade

    now = datetime.datetime.now() #variavel com a data de hoje

    this_year = now.year # ano atual

    print(name + 'neste'  + str(this_year - age + 100) + 'ano terei 100 anos') 
    print()
    in_program = input("Voce Deseja continuar, se não digite 0 para sair：") # opção de continuar

    if in_program == '0':
        break
