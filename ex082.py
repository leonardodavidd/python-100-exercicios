#Faça um programa que leia 5 valores e guarde em uma lista
#No final mostrar quem foi o menor e maior valor e a sua posição na lista
listinha = []
menor = 99999999
maior = 0
posicao1 = 0
posicao2 = 0

for c in range(0,5):
    listinha.append(int(input('Digite um número')))
    if listinha[c] > maior:
        maior = listinha[c]
        posicao1 = c
    if listinha[c] < menor:
        menor = listinha[c]
        posicao2 = c
print(f'Valores digitados {listinha}')
print(f'Maior valor {maior} na posição {posicao1+1}')
print(f'Menor valor {menor} na posição {posicao2+1}')

