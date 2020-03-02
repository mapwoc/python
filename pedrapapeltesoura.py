'''
Jogo do papel, pedra tesoura
'''


user_one = input("nome jogador 1:")
user_two = input("nome jogador 2:")
while True:
    # Input 
    try:
        user_one_answer = int(input("{}, Por favor Escolha:\n1.Pedra\n2.Tesoura\n3.Papel\n".format(user_one)))
        user_two_answer = int(input("{}, Por favor Escolha:\n1.Pedra\n2.Tesoura\n3.Papel\n".format(user_two)))
        # Check input
        if user_one_answer not in range(1,4) or user_two_answer not in range(1,4):
            print("Entrada fora das opções")
            continue
    except:
        print("Entrada errada.")
        continue
    # Compare
    if user_one_answer + 1 == user_two_answer or user_one_answer - 2 == user_two_answer:
        print("{} Ganhou!".format(user_one))
    elif user_one_answer == user_two_answer:
        print("Novamente.")
    else:
        print("{} Ganhou!".format(user_two))
    # Start a new game
    try:
        if int(input("Insira o numero 1 para iniciar um novo jogo, or ou qualquer outro para sair.")) == 0:
            break
    except:
        print("Entrada errada. Jogo Saiu.")
        break
    
