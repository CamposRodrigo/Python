import  math
x = float(input('Digite o angulo que voce quer: '))
seno = math.sin(math.radians(x))
print('O Seno do angulo de {} sera {:.2f} .'.format(x,seno))
cos = math.cos(math.radians(x))
print('O Cosseno do angulo de {} sera {:.2f} .'.format(x,cos))
tg = math.tan(math.radians(x))
print('A Tangente do angulo de {} sera {:.2f} .'.format(x,tg))