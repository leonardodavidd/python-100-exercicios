#Programa que verifica quando se deve realizar o alistamento miliar
#Programa fala se já está na hora, se ja passou da hora ou se ainda não chegou a hora / e mostra o tempo disso tudo
ano = int(input('Digite o seu ano de nascimento '))
verificar = 2022 - ano
print('Quem nasceu em {} tem {} anos em 2022'.format(ano, verificar,))
if verificar < 18:
    conta = 18 - verificar
    print('Você ainda irá se alistar daqui {} anos'.format(conta))
elif verificar == 18:
    print('Você já tem 18 anos e deve se alistar imediatamente')
elif verificar > 18:
    conta = verificar - 18
    print('Já passou o prazo para vc se alistar de {} anos'.format(conta))
