#Exemplo de criação de tabuada
n = int(input(' Digite um número que vc quer para exibir sua tabuada'))
cont = 0
for c in range(1,11):
    cont = cont + 1
    tabuada = n * cont
    print(' {} X {} = {} '.format(n, cont, tabuada))
print(' FIM ')


