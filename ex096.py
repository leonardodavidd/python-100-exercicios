#leia o nome e média de um aluno e guarde em um dicionário
#No final mostrar se o aluno foi aprovado ou não diante da media
dicionario = {}
dicionario['aluno'] = str(input('Digite seu nome: '))
dicionario['media'] = float(input('Digite sua média: '))
if dicionario['media'] >= 6:
    print('Você foi aprovado')
else:
    print('Você foi reprovado / está de recuperação')
