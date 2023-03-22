#Exemplo de pagamento de produto com valor original, ou valor com acréscimo ou desconto
valor = float(input('Digite o valor a ser pago pelo produto'))
print('*' * 20)
print('Condições de pagamento')
print('1-A vista dinheiro ou cheque ganha 10 % de desconto')
print('2-A vista no cartão : 5 % de desconto')
print('3-Em até 2x no cartão : preço normal')
print('4-Parcelado 3x ou mais no cartão: 20 % de juros')
print('*' * 20)
cod = int(input('Digite a opção que você deseja ! 1 a 4 !'))
if cod == 1:
    desconto = valor * 0.10
    print('Valor original sem desconto {:.2f} , valor que você irá pagar com desconto {:.2f}'.format(valor, (valor-desconto)))
elif cod == 2:
    desconto = valor * 0.05
    print('Valor original sem desconto {:.2f}, valor que você irá pagar com desconto {:.2f}'.format(valor, (valor-desconto)))
elif cod == 3:
    print('O valor que você irá pagar será o preço original de {:.2f}'.format(valor))
elif cod == 4:
    juros = valor * 0.20
    print('O valor original sem desconto {:.2f}, valor que você irá pagar com os juros aplicados {:.2f}'.format(valor, (valor+juros)))
else:
    print('O valor não foi encontrado ! Verifique as alternativas !')





