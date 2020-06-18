salario = float(input('Digite o salario do funcionario R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)

else:
    novo = salario + (salario * 10 /100)
print('O salario de R${:.2f} passa a ser de R${:.2f}'.format(salario, novo))
