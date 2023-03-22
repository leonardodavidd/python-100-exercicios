#Crie um programa que o usuário pode digitar vários números e armazene em uma lista
#Coloque os valores no final em ordem crescente
lista = []
while True:
    lista.append(int(input('Digite um número ')))
    oi = str(input('Digite S para continuar ou N para sair')).upper().strip()[0]
    if oi == 'N':
        break
lista.sort()
print(f'Os números em ordem crescente são {lista}')
