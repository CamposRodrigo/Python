x = float(input('Digite o valor do produto: R$'))
print('Na liquidacao esse produto de R${:.2f} voce so vai pagar R${:.2f}'.format(x, x-(5 / 100) * x))

