#Exemplo24 comando upper = colocar tudo maiusculo
#comando strip remover espaços da frase para nao alterar resultados
#frase.count contar quantas vezes aparece a letra A
#frase.find ver qual é a primeira vez que aparece
#frase.rfind ver qual é a ultima vez que aparece

frase = str(input('Digite uma frase')).strip().upper()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A letra A aparece na posição {} pela primeira vez'.format(frase.find('A')))
print('A letra A aparece na posição {} pela última vez'.format(frase.rfind('A')))



