#Leia 6 números e faça a soma apenas dos números pares digitados
#Se for ímpar, desconsiderar !
soma = 0
for c in range(1,7):
   n = int(input(' Digite um número '))
   if n % 2 == 0:
       soma += n
print(' A soma de todos os valores pares digitados é de : {} '.format(soma))
