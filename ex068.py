#Vamos gerar um exeplo de uma sequencia com termo e razao PA
#O comando end = ' ' faz com que nós conseguimos mostrar todos os resultados na mesma linha, sem pular linha
print('*' * 20)
print('Gerador de PA')
print('*' * 20)
primeiro = int(input('Primeiro termo'))
razao = int(input('Razão da PA'))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} ,'.format(termo), end='')
    termo = termo + razao
    cont = cont + 1
print('Fim')
