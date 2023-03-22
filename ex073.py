#lEIA O NOME E O PREÇO DE VÁRIOS PRODUTOS
#O PROGRAMA PERGUNTA SE VC QUER CONTINUAR SIM OU NÃO
total = 0
cont = 0
menor = 1000000
while True:
    nome = str(input('Digite o nome do produto !'))
    preco = float(input('Digite o preço do produto !'))
    continuar = str(input('Deseja continuar S para sim N para não')).strip().upper()[0]
    total = total + preco
    if preco > 1000:
        cont += 1
    if preco < menor:
        menor = preco
        nome2 = nome
    if continuar == 'N':
        break
print(f'O total gasto na compra foi de {total}')
print(f'Quantos produtos custam mais de 1000 reais? {cont}')
print(f'Qual é o nome do produto mais barato ? {nome2}')



