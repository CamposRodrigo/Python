km = float(input('Digite a distancia em Km da sua viagem: '))
if km <200:
    print('Sua viagem ira comecar!!!!')
    print('O preco da passagem sera de R${}'.format(km*0.5))
else:
    print('Sua viagem ira comecar!!!!')
    print('O preco da passagem sera de R${:.2f}'.format(km*0.45))