'''
marcos dias
'''

def fibo_generate(number):
    fibo = [1, 1]
    for i in range(0, number - 2):
        fibo.append(fibo[i] + fibo[i+1])
    return fibo

def check_input(number):
    try:
        if int(number) > 0:
            return (True, int(number))
    except:
        return False

def get_input():
    input_number = input('Quantos numeros Fabonacci pode ser gerados?')
    return check_input(input_number)

# Inicialização
check_status = get_input()
# Loop
while check_status[0]:
    print(fibo_generate(check_status[1]))
    # A new turn
    check_status = get_input()


