velocidade = float(input('Qual e a velocidade do seu carro? '))
if velocidade > 80:
    print('MULTADO!! Voce excedeu o limite de velocidade que e de 80km/h .')
    print('Voce tera que pagar uma multa de R${:.1f}'.format((velocidade - 80)* 7))
else:
    print('Tenha um bom dia .Dirija com Cuidado!!!')