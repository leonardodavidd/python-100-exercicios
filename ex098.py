#crie um programa que leia o nome, ano de nascimento e carteira de trab e cadastre em um dicionário
#Caso a CTPS for diferente de 0 o dicionário receberá também o ano de contratação e o salário.
#calcule e acrescente além da idade, com quantos anos a pessoa irá se aposentar = Identifique geral para 35 anos de trab
from datetime import datetime
lista1 = {}
lista2 = {}
lista1['nome'] = str(input('Digite seu nome '))
lista1['ano'] = int(input('Digite seu ano de nascimento '))
lista1['carteira'] = int(input('Digite sua carteira de trabalho - 0 CASO NÃO TENHA '))
if lista1['carteira'] == 0:
    print(f'Nome tem o valor {lista1["nome"]}')
    print(f'Idade tem o valor {datetime.now().year - lista1["ano"]}')
    print(f'ctps tem o valor {lista1["carteira"]}')
else:
    lista2['contratacao'] = int(input('Qual o seu ano de contratação ? '))
    lista2['salario'] = float(input('Qual o seu salário ? '))
    lista2['aposentadoria'] = (lista2['contratacao'] - datetime.now().year) + 35
    print(f'Nome tem o valor {lista1["nome"]}')
    print(f'Idade tem o valor {datetime.now().year - lista1["ano"]}')
    print(f'ctps tem o valor {lista1["carteira"]}')
    print(f'contratação tem o valor {lista2["contratacao"]}')
    print(f'salário tem o valor {lista2["salario"]}')
    print(f'aposentadoria tem o valor {lista2["aposentadoria"] + datetime.now().year - lista1["ano"]}')
