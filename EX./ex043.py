peso = float(input('Qual e o seu peso ? '))
altura = float (input('Qual e a sua altura ? '))
imc = peso / altura**2
if imc < 18.5 :
    print('Seu IMC e {:.1f} .Esta abaixo do Peso.'.format(imc))
elif  18.5 <= imc < 25:
    print('Seu IMC e {:.1f} .Esta no Peso Ideal.'.format(imc))
elif  25 <= imc < 30:
    print('Seu IMC e {:.1f} .Esta com Sobrepeso.'.format(imc))
elif  30 <= imc < 40:
    print('Seu IMC e {:.1f} .Esta com Obesidade.'.format(imc))
else:
    print('Seu IMC e {:.1f} .Esta com Obesidade Morbida.'.format(imc))
