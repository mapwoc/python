#nome completo vira so dois
nomeCompleto = str(input('Digite seu nome completo: ')).strip()
nomeDividido = nomeCompleto.split();

print('O primeiro nome é {} e o ultimo é {}'.format(nomeDividido[0], nomeDividido[len(nomeDividido) - 1]))
