x = int(input('Primeiro termo: '))
y = int(input('Razao: '))
decimo = x +(10-1)* y
for c in range(x,decimo + y ,y):
    print('{}'.format(c), end=" -> ")
print('Acabou')