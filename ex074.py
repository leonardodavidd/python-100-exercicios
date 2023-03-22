#Leia quatro valores pelo teclado
#Guarde os valores em uma tupla
#Quantas vezes apareceu o valor 9 ?
#Em que posição foi digitado o primeiro valor 3 ?
#Quais foram os números pares ?
soma = 0
tupla = (int(input('Digite um número')), int(input('Digite um número')), int(input('Digite um número')),
         int(input('Digite um número')))
print(f'Valores digitados e armazenados na TUPLA: {tupla}') #mostrar valores digitados
print(f'Quantidade de vezes que apareceu o número 9: {tupla.count(9)}') #comando count conta quantas vezes aparece
if 3 in tupla:
    print(f'Em que posição foi digitado o valor número 3: {tupla.index(3)+1}') #comando index conta a posição que está
else:
    print(f'O valor 3 não foi digitado !')
for c in tupla:
    if c % 2 == 0:
        print('\nnúmero par digitado',c, end='')

