num = [[], []]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}o. valor:'))
    if valor % 2 == 0 :
        num[0].append(valor)
        num[0].sort()
    else:
        num[1].append(valor)
        num[1].sort()
print('=-'*30)
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitados foram: {num[1]}')
