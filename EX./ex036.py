print('-=-'*20)
print('\033[36;40m         PROGRAMA PARA FINANCIAMENTO DE CASA PROPRIA\033[m')
print('-=-'*20)
casa = float(input('Qual o valor da casa ? R$ '))
salario = float(input('Qual o seu salario mensal? R$ '))
financiamento = int(input('Em quantos anos voce quer financiar sua casa? ==>> '))
meses = financiamento * 12
cal = casa / meses
if cal <= salario * 30 / 100 :
    print('\033[31;42m FINANCIAMENTO APROVADO!!! Serao {} parcelas  DE R${:.2f}\033[m'.format(meses,cal))
else:
    print('\033[31;42mDesculpe a parcela para esse financiamento excede 30%\033[m \n\033[31;42mde seu salario!!!!'
          'A parcela seria de R${:.2f} e seu \033[m \n\033[31;42msalario e de apenas R${:.2f}\033[m'.format(cal,salario))
