#Exemplo18 Sortear algum aluno para apresentar o trabalho
import random
n1 = str(input('Digite o primeiro aluno'))
n2 = str(input('Digite o segundo aluno'))
n3 = str(input('Digite o terceiro aluno'))
n4 = str(input('Digite o quarto aluno'))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))


