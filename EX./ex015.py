x = int(input('Quantos dias o carro ficou alugado? '))
y = float(input('Quantos quilometros voce andou? Km'))
print('Voce usou o carro por {}dias e andou por km{} .Voce tem que pagar R${:.2f} .'
      .format(x,y,(x*60)+(y*0.15)))
