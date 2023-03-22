#Crie um programa que sorteie 5 números aleatórios e guarde em uma tupla
#Depois disso, gerar na tela os números sorteados e qual é o maior e qual é o menor número
from random import randint

tupla = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Os valores sorteados foram: {tupla}')

for c in tupla:
    print(f'{c}', end='')
print(f'\nO maior número sorteado foi {max(tupla)}')
print(f'O menor número sorteado foi {min(tupla)}')

