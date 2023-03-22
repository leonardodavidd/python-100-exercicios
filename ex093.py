#exercicio mega sena
from random import randint
lista = []
jogos = []
total = 1
print('*' * 20)
print('Mega sena ! ')
print('*' * 20)
numeros = (int(input('Digite quantas vezes você quer sortear números para mega-sena')))
while total <= numeros:
    cont = 0
    while True:
        num = randint(0, 60)
        if num not in lista:
            lista.append(num)
            cont = cont + 1
            if cont >= 6:
                break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total = total + 1
for i, l in enumerate(jogos):
    print(f' jogo {i}: {l}')


