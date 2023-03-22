#exemplo24 Criar um programa e ver se o valor digitado tem a palavra 'SILVA'
#Dá para resolver utilizando nome.upper para colocar tudo maíusculo ou nome.lower para colocar tudo minusculo
#depois verificar se há ''silva'' digitado

nome = str(input('Digite o seu nome')).strip()
print('Seu nome tem silva ? {}'.format('SILVA' in nome.upper()))








