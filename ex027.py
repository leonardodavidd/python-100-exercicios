#Exemplo19 Sortear a ordem de apresentação dos alunos
from random import shuffle
n1 = str(input('Primeiro aluno'))
n2 = str(input('segundo aluno'))
n3 = str(input('terceiro aluno'))
n4 = str(input('quarto aluno'))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentaçãos será')
print(lista)
