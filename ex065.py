#Leia o sexo M/F , so aceite esses dados, se o usuário digitar errado
#peça a digitação novamente até ter um valor correto
sexo = str(input('Digite o seu sexo M/F')).strip().upper()[0]
print(sexo)
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, pvf informe seu sexo')).strip().upper()[0]
print('Sexo {} formatado com sucesso'.format(sexo))
