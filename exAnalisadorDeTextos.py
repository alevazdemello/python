nome = str(input('Digite o seu nome completo: '))
print('Analisando seu nome...')
print(f'Seu nome em maísculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
espacos = (nome.count(' '))
print(f'Seu nome tem ao todo {len(nome) - espacos} letras.')
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
#outra forma de contar o n° de letras
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))
