salario = int(input('Digite o seu salário'))
if salario > 1250:
    aumento = salario * 0.10
    valortotal = salario + aumento
if salario <= 1250:
    aumento = salario * 0.15
    valortotal = salario + aumento

print('O salário foi de {:.2f}, o aumento foi de {:.2f}, valor total foi de {:.2f} '.format(salario, aumento, valortotal))

