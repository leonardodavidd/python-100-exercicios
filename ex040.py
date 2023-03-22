#Faça um programa que peça 3 digitos e analise qual número é o maior ou menor
n1 = int(input('Digite um número'))
n2 = int(input('Digite um número'))
n3 = int(input('Digite um número'))
#Achando o maior número
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
#Achando o menor número
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O maior número foi {}'.format(maior))
print('O menor número foi {}'.format(menor))
