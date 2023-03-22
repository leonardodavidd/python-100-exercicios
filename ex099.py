#Exemplo usando apenas variaveis simples e dicionários !
jogar = {}
jogar['nome'] = str(input(f'Qual o seu nome ?'))
jogar['quantidade de partidas'] = int(input(f'Quantas partidas vc jogou {jogar["nome"]} ?'))
soma = 0
for c in range(0, jogar["quantidade de partidas"]):
    jogar['quantidade de gols'] = int(input(f'Quantos gols foram feitos na partida {c+1} ? '))
    soma = soma + jogar['quantidade de gols']
print(jogar['nome'], f' , Quantidade de partidas jogadas:', jogar['quantidade de partidas'], f' -> quantidade de gols marcados : {soma}')
print()





