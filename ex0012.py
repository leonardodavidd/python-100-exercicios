#Exemplo9 Como calcular um DESCONTO ??
preco = float(input('Digite o valor do preço atual'))
desconto = preco * 0.05
valorfinal = preco - desconto
input('O produto que custava {:.2f}, na promoção com desconto de 5% vai custar {:.2f} ! '.format(preco, valorfinal))

