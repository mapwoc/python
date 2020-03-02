n1 = float(input('digite a 1a nota '))
n2 = float(input('digite a 2a nota '))
n3 = float(input('digite a 3a nota '))
n4 = float(input('digite a 4a nota '))
media = (n1 + n2 + n3 + n4) /4
print (media)
if media >= 6:
    print('passou de ano')
    #if 3 <= nf and nf < 5:
elif 4 <= media and media < 6:
    print('Ficou de Exame')
else:
    print('reprovou por nota')