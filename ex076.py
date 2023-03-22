#Crie uma tupla com contagem regressiva do 0 até o 20
tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número'))
    if num >= 0 and num <= 20:
        break
    print('Tente novamente', end='')
print(f'Você digitou o número {tupla[num]}')
   








