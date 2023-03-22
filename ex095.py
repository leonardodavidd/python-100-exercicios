#primeiros exemplos de DICIONÁRIOS ! SÃO FEITOS POR = {}
#comando del apagar algo = del pessoas['sexo'], keys ver as chaves, values ver os valores e items ver tudo
#se quiser adicionar algo em um dicionário nao e preciso append, basta seguir exemplo abaixo
#pessoas['peso'] = 98
pessoas = {'nome': 'gustavo', 'sexo':'M', 'idade': 23 }
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.values():
    print(k)
for k in pessoas.keys():
    print(k)
for k in pessoas.items():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')





