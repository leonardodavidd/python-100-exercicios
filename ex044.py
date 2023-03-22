#Exemplo de programa que calcula emprestimo bancario para compra de uma casa.
#Se o valor da prestação mensal ultrapassar 30 % do salário mensal o empréstimo é negado.
valor = int(input('Digite o valor da casa que vc quer comprar'))
salario = float(input('Digite o seu salário mensal'))
anos = int(input('Em quantos anos deseja pagar a casa ?'))

prestacao = valor / (anos * 12)
porcentagem = salario * 0.30

if prestacao < porcentagem:
    print('Empréstimo concedido !')
    print('O valor da casa é de {:.2f} , o salário do comprador é {:.2f}, prestação mensal valor de {:.2f} reais em {:.2f} anos.'.format(valor, salario, prestacao, anos))
else:
    print('Seu empréstimo foi negado porque ultrapassou 30% do seu salário mensal !')

