print('      -=-'*20)
print('                                      REDE DE LOJAS CAMPOS')
print('      -=-'*20)
x = float(input('Digite o valor da compra1: R$'))
print('CONDICOES DE PAGAMENTO:')
print('[1]- A vista dinheiro/cheque\n'
      '[2]- A vista no cartao\n'
      '[3]- Em ate 2x no cartao\n'
      '[4]- Em 3x ou mais no cartao')
y = int(input('Digite a sua opcao: '))
if   y == 1:
    print('O valor da sua compra sera de R${:.2f} .'.format(x-x*10/100))
elif y == 2:
    print('O valor da sua compra sera de R${:.2f} .'.format(x-x*5/100))
    print('rr')
elif y == 3:
       a = int(input('Quantas parcelas?'))
       print('Voce parcelou em {} vezes.\n'
             'Suas parcelas serao no valor de R${:.2f} .\n'
             'O valor da sua compra sera de R${:.2f}'.format(a,(x+x*20/100)/a,x+x*20/100))
elif y == 4:
    print('O valor da sua compra sera de R${:.2f} .'.format(x))
else:
    print('Opcao invalida!!!')





