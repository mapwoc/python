'''
marcos dias
maior ou menor
numa lista a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] faça um programa que verifica
quais numero na lista são menores que 5


'''

input_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Solution
print("Solution")

for i in input_list:
    if i < 5:
        print(i)
        
# Extras
print("Extras")

cut_off = int(input("Insira um numero de corte:"))
new_list = [i for i in input_list if i < cut_off]
print(new_list)
