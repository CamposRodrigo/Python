n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
x = (n1 +n2 )/2
if 7>x >= 5:
    print('Tirando {} e {} ,Sua media e {} , Voce ficou de RECUPERACAO!!!!'.format(n1,n2,x))
elif x >= 7:
    print('Tirando {} e {} ,Sua media e {} , Parabens voce esta APROVADO!!!.'.format(n1,n2,x))
else:
    print('Tirando {} e {} ,Sua media e {} , Voce esta REPROVADO!!!!!'.format(n1,n2,x))
