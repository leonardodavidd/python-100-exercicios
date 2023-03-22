#Crie um programa que o usuário pode digitar vários números e guardar estes números em uma lista
#Crie uma lista para os numeros pares, uma lista para os números impares, 3 listas no final
lista = []
lista1 = []
lista2 = []
while True:
    lista.append(int(input('Digite um número')))
    comando = str(input('Digite S para continuar ou N para sair')).strip().upper()[0]
    if comando == 'N':
        break
for c, v in enumerate(lista):
    if v % 2 == 0:
        lista1.append(v)
    if v % 2 == 1:
        lista2.append(v)
print(f'Números da lista {lista}')
print(f'Números da lista pares {lista1}')
print(f'Números da lista inpares {lista2}')



