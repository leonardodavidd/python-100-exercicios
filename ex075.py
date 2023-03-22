#Times do campeonato brasileiro armazenados em uma TUPLA
#Quem são os 5 primeiros ?
#Quem são os 3 primeiros ?
#Quem são os ultimos 4 ?
#Como colocar os times em ordem alfabética
#Em que posição está o time do vasco?

time = ('corinthians', 'palmeiras', 'gremio', 'vasco', 'fluminense', 'santos')
print(f'lista de times {time}') # Estou mostrando TODOS os times inclusos na TUPLA aqui
print(f'Os 5 primeiros são {time[0:5]}')
print(f'Os 3 primeiros são {time[0:3]}')
print(f'Quem são os 4 últimos ? {time[-4:]}')
print(f'Os times em ordem alfabética são {sorted(time)}')
print(f'O Vasco da Gama está na posição {time.index("vasco")+1}')

