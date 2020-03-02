'''
Exercise 4: Divisores 

crie um progrma que faça a divisão de um numero por ele mesmo e seus divisores comuns
exemplo 4 são divisiveis por 4, 2 e 1 

'''

# Solution
number = int(input("Insira um numero :"))
divisores = [i for i in range(1, number+1) if number % i == 0]

print("Divisor(es):")
print(divisores)
