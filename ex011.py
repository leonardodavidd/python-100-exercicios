#Exemplo8 Como calcular área ?
larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a  altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {} x {} e sua área é de: {} '.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede vc precisa de {} l de tinta'.format(tinta))

