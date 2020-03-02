'''
Gerador de Senhas

'''

def generate_passwords(level): #
    import string
    import random
    
    level_dict = {'curta':8, 'media':12, 'dificil':16} #define tamanhos caracteres de cada nivel de senha
    
        segment = [0, 0, 0, 0]
    for x in range(level_dict[level]):
        r = random.randint(0,3)
        segment[r] += 1
    
    lower_letter = random.choices(string.ascii_lowercase, k=segment[0])#letras minusculas randomicas
    upper_letter = random.choices(string.ascii_uppercase, k=segment[1])#letras maiusculas randomicas
    
    digits = random.choices(string.digits, k=segment[2])
    symbols = random.choices('!@#$%^&*()_+', k=segment[3])
    
    password = lower_letter + upper_letter + digits + symbols
    random.shuffle(password)
    
    return ''.join(password)
'''
Verifica nivel da senha gerada
'''
def check_level_input(string, level):
    if string.lower() == level or string.lower() == level.lower()[0]:
        return True
    else:
        return False
'''
Escolha do tipo de senha
'''
def main():
    while True:
        level = input('escolha um nivel de Senha: [curta/media/dificil] ou digite exit para sair ')
        if level.lower() == 'exit':
            break
        elif check_level_input(level, 'curta'):
            print(generate_passwords('curta'))
        elif check_level_input(level, 'media'):
            print(generate_passwords('media'))
        elif check_level_input(level, 'dificil'):
            print(generate_passwords('dificil'))
        else:
            print('Erro de Input')
                
if __name__ == "__main__":
    main()


