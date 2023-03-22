#Refazendo o exercicio dos triangulos
#Verificar qual o tipo de triangulo formado pelos dados digitados
r1 = float(input('Digite o 1 número'))
r2 = float(input('Digite o 2 número'))
r3 = float(input('Digite o 3 número'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os elementos podem formar um triângulo')
    if r1 == r2 and r1 == r3:
        print('Triângulo equilátero formado !')
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print('Triangulo escaleno formado !')
    else:
        print('Triangulo isósceles formado !')
else:
    print('Os elementos acima não formam um triângulo')
