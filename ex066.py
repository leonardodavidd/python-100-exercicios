#leia dois valores
#escolher alguma opção do menu
valor = int(input('Digite um valor '))
valor1 = int(input('Digite outro valor valor '))

soma = 0
print('*'*20)
print('Opção 1:somar')
print('Opção 2:multiplicar')
print('Opção 3:maior')
print('Opção 4:novos números')
print('Opção 5:sair do programa')
print('*'*20)
escolha = 0

while escolha != 5:
    escolha = int(input('Digite a alternativa que vc deseja'))
    if escolha == 1:
        soma = valor + valor1
        print('A soma é {}'.format(soma))
    elif escolha == 2:
        multiplicacao = valor * valor1
        print('O resultado da multiplicação é de {}'.format(multiplicacao))
    elif escolha == 3:
        if valor > valor1:
            maior = valor
        else:
            maior = valor1
        print('O maior número digitado foi de {}'.format(maior))
    elif escolha == 4:
        print('Informe os valores novamente')
        valor = int(input('Digite um valor '))
        valor1 = int(input('Digite outro valor valor '))
    elif escolha == 5:
        print('*' * 20)
        print('Finalizando...')
        print('*' * 20)



