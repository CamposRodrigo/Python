valores = []
pares = []
impares = []
while True:
    c = int(input('Digite um valor: '))
    valores.append(c)
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
    r = str(input('Quer continuar? [S/N]: '))
    if r in 'Nn':
        break

print('=-'*20)
print(f'A lista completa é {valores}.')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')