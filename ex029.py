#Exemplo21 Como digitar nome maiúsculo e minusculo , contar todos os dígitos do nome sem contar os espaços
#Falar quantas letras tem o primeiro nome
nome1 = str(input('Digite seu nome !')).strip()
print('Seu nome em maiúsculo é {}'.format(nome1.upper()))
print('Seu nome em minusculo é {}'.format(nome1.lower()))
print('Seu nome ao todo tem {} digitos'.format(len(nome1) - nome1.count(' ')))
#print('Seu primeiro nome tem {} digitos'.format(nome1.find(' ')))
separa = nome1.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))















