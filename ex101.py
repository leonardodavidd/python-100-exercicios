#Exemplo usando apenas variaveis simples e dicionários !
jogar = {}
soma = 0
questao = 'S'
print('-' * 30)
print('Iniciando o programa ... ')
print('-' * 30)
while questao == 'S':
    questao = str(input('Olá ! Digite S para continuar no programa ou N para sair ! ')).strip().upper()[0]
    if questao != 'NS':
        print('Código inválido ! ')
        questao = str(input('Olá ! Digite S para continuar no programa ou N para sair ! ')).strip().upper()[0]
    if questao == 'N':
        print('Finalizando .... xd')
        break
    if questao == 'S':
        del soma
        soma = 0
        jogar['nome'] = str(input(f'Qual o seu nome ?'))
        jogar['quantidade de partidas'] = 0
        jogar['quantidade de partidas'] = int(input(f'Quantas partidas vc jogou {jogar["nome"]} ?'))
        for c in range(0, jogar['quantidade de partidas']):
            jogar['Quantidade de gols'] = int(input(f'Quantos gols foram feitos na partida {c + 1} ? '))
            soma = soma + jogar['Quantidade de gols']
        print(jogar["nome"], f' / quantidade de partidas :', jogar["quantidade de partidas"], f' -> total de gols marcados: {soma}')
        print()












