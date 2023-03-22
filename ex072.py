#Exemplo análise de dados de grupo
soma = 0
soma2 = 0
soma3 = 0
while True:
    idade = int(input('Digite a sua idade !'))
    sexo = str(input('Digite o seu sexo M para masculino e F para feminino !')).strip().upper()[0]
    continuar = str(input('Digite S para continuar ou N para sair')).strip().upper()[0]
    if idade >= 18:
        soma = soma + 1
    if sexo == 'M':
        soma2 = soma2 + 1
    if sexo == 'F' and idade < 20:
        soma3 = soma3 + 1
    if continuar == 'N':
        break
print('Quantas pessoas tem mais de 18 anos ? {} '.format(soma))
print('Quantos homens foram cadastrados ? {} ' .format(soma2))
print('Quantas mulheres tem menos de 20 anos ? {} '.format(soma3))
