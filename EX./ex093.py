jogador = {}
partida= []
jogador['Nome']= str(input('Digite o nome do Jogador: '))
tot= int(input(f'Quantas partidas {jogador["Nome"]} jogou ? '))
for c in  range(0,tot):
    partida.append( int(input(f'Quantos gols na partida {c}: ')))
jogador['gols']= partida[:]
jogador['total']= sum(partida)
print('=-'*30)
print(jogador)
print('=-'*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v} .')
print('=-'*30)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador["gols"]):
    print(f'     ==>Na partida {i} fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')