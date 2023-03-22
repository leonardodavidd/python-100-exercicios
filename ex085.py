#Crie um programa que leia vários números digitados pelo usuário e guarde em uma lista
#Mostre: Quantos números foram digitados / A lista de valores ordenado de forma decrescente
#Se o valor 5 foi digitado sim ou não na lista
cont = 0
valor = ''
lista = []
while True:
    lista.append(int(input('Digite um número')))
    comando = str(input('Digite S para continuar ou N para sair')).strip().upper()[0]
    cont += 1
    if comando == 'N':
        break
    if 5 in lista:
        valor = 'Verdadeiro'
    else:
        valor = 'Falso'
lista.sort(reverse=True)
print(f'Quantidade de números digitados {cont}')
print(f'Lista de valores ordenados de ordem decrescente {lista}')
print(f'O valor 5 foi digitado na lista ? Resposta: {valor} ')



