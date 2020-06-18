maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input("Peso da {} pessoa : ".format(p)))
    if peso > maior:
        maior = peso

    if p == 1 or peso < menor:
        menor = peso

print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))