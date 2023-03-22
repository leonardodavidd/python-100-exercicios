#O usuário só pode digitar 7 valores, cadastrar esses valores em uma única lista
#No final mostrar valores ímpares e pares separados , em ordem crescente
lista = [[], []]
for c in range(0, 7):
    valor = int(input('Digite um valor ! '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
sorted(lista[0])
sorted(lista[1])
print(f'Os valores pares são {lista[0]}')
print(f'Os valores ímpares são {lista[1]}')
