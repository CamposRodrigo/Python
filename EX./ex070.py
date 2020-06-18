tot = v = j = cont =0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preco: R$'))
    cont += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    if preco > 1000:
        v += 1
    tot += preco
    decisao = ' '
    if decisao != 'SN':
        decisao = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if decisao == 'N':
            break
print(f'Total da compra foi R$\033[31m{tot:.2f}\033[m')
print(f'Temos \033[31m{v}\033[m produto custando mais de R$1000.00')
print(f'O produto mais barato foi \033[31m{barato}\033[m que custa \033[31mR${menor}\033[m')


