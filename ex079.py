#Crie um programa que tenha uma tupla com nomes dos produtos e seus preços
#Organizar dados no final de modo tabular

lista = ('lapis', 1.50,
         'caneta', 2.10,
         'tesoura', 5.50,
         'caderno', 9.90,
         'borracha', 10)
for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<30}', end='')
    else:
        print(f'RS {lista[c]:>7.2f}')



