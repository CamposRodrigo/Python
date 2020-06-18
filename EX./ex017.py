from math import hypot
x = float(input('Qual comprimento do cateto oposto? '))
y = float(input('Qual comprimento do cateto adjacente? '))
h = hypot(x,y)
print('O valor da hipotenusa e {:.2f} .'.format(h))