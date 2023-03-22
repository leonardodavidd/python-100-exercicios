#Exemplo25 Como achar/identificar o primeiro nome digitado e o ultimo nome digitado ?
n = str(input('Digite o seu nome completo')).strip()
nome = n.split()
print('Seu primeiro nome é {} '.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))




