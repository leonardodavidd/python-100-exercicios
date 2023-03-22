#Leia a velocidade de um carro
#Se ultrapassar 80 km , aparece uma mensagem dizendo vc foi multado
velocidade = int(input('Digite a velocidade do carro'))
if velocidade >= 80:
    print('Você foi multado, valor:{:.2f}'.format(velocidade * 7))
else:
    print('Você não foi multado')
