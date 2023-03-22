#Crie um programa onde o usuário pode digitar 5 números, armazene em uma lista
#Coloque a lista ordenada na tela

lista = []
for c in range(0,5):
    lista.append(int(input('Digite um valor')))
lista.sort()
print(f'Os valores ordenados são {lista}')
