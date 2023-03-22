#Exemplo26
km = float(input('Digite a quantidade de KM percorrido'))
dias = int(input('Digite a quantidade de dias que o carro foi alugado'))
preco = (60 * dias) + (km * 0.15)
print('O valor a ser pago pelo carro é de {:.2f} '.format(preco))
