#Leia o peso de 5 pessoas.No final mostre quem foi o menor peso e quem foi o maior peso

maior = 0
menor = 1000000
for c in range(0, 5):
    numero = float(input(' Digite o seu peso em KG'))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print('O maior número foi de {}, o menor número foi de {} !'.format(maior,menor))


