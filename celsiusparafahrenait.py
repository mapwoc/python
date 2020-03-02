#Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
tCelcius = float(input('Digite uma temperatura em graus celcius: '))

tFahrenheits = tCelcius * 9 / 5 + 32;

print('A temperatura de {} graus celcius equivale a {} graus Fahrenheits'.format(tCelcius, tFahrenheits))

