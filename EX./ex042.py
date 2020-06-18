n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < n1 + n3 and n2 < n1 +n3 and n3 < n1 + n2:
    print('Os segmentos podem formar um triangulo.')
    if n1 == n2 == n3 == n1 :
        print('EQUILATERO')
    elif n1 != n2 != n3 != n1:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('Os segmentos acima NAO PODEM FORMAR triangulo.')