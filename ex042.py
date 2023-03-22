#Verificando se os dados digitados podem formar um triângulo
r1 = float(input('Digite o 1 número'))
r2 = float(input('Digite o 2 número'))
r3 = float(input('Digite o 3 número'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triangulo !')
else:
    print('Os segmentos NÃO podem formar um triangulo !')


