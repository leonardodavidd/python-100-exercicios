#Leia nome e peso de várias pessoas, guarde em uma lista
#Mostrar quantas pessoas foram cadastradas, mostrar quem foram as pessoas mais pesadas
#Mostrar quem foram as pessoas mais leves
resp = 's'
lista = []
lista1 = []
cont = 0
maior = 0
menor = 1000000
while resp != 'N':
    lista.append(str(input('Digite o seu nome ')))
    lista.append(float(input('Digite o seu peso ')))
    resp = str(input('Digite S para continuar ou N para sair')).strip().upper()
    cont = cont + 1
    lista1.append(lista[:])
    lista.clear()
    for c in lista1:
        if c[1] > maior:
            maior = c[1]
        elif c[1] < menor:
            menor = c[1]
for c in lista1:
    if c[1] == maior:
        print(f'{c[0]}')
print(f' Pessoa(s) mais pesada(s) com {maior} kilos, citada acima ')
for c in lista1:
    if c[1] == menor:
        print(f'{c[0]}')
print(f'Pessoa(s) mais leve(s) com {menor} kilos, citada acima ')
print(f'Total de pessoas cadastradas no sistema: {cont}')

