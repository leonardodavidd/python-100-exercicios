#programa sorteia 4 jogadores que jogam um dado e tem resultados aleatórios
#No final colocar em ordem, sabendo que o vencedor é o maior número dado
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Os valores sorteados foram: ')
for k, v in jogo.items():
    print(f'O jogador {k} sorteou o número {v}')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('Ranking:')
for i , v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')
    sleep(1)

