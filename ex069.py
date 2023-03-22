#Vamos gerar um exeplo de uma sequencia com termo e razao PA
#O comando end = ' ' faz com que nós conseguimos mostrar todos os resultados na mesma linha, sem pular linha
print('*' * 20)
print('Gerador de PA')
print('*' * 20)
primeiro = int(input('Primeiro termo'))
razao = int(input('Razão da PA'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ,'.format(termo), end='')
        termo = termo + razao
        cont = cont + 1
    print('Fim')
    mais = int(input('Quantos termos você quer mostrar a mais ?'))
print('Progressão finalizada com {} termos mostrados'.format(total))
