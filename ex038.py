distancia = int(input('Digite a distancia percorrida em KM'))
if distancia <= 200:
    print('O valor pago foi de {:.2f}'.format(distancia * 0.50))
else:
    print('O valor pago foi de {:.2f}'.format(distancia * 0.45))


