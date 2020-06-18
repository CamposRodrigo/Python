from datetime import date
idade = int(input('Digite seu ano nascimento: '))
x = date.today().year - idade
if   x <= 9:
    print('Esse atleta tem {} anos,\nEsta na categoria ==>> MIRIM <<== .'.format(x))
elif x <=14:
    print('Esse atleta tem {} anos,\nEsta na categoria ==>> INFANTIL <<== .'.format(x))
elif x <=19:
    print('Esse atleta tem {} anos,\nEsta na categoria ==>> JUNIOR <<== .'.format(x))
elif x <=25:
    print('Esse atleta tem {} anos,\nEsta na categoria ==>> SENIOR <<== .'.format(x))
else:
    print('Esse atleta tem {} anos,\nEsta na categoria ==>> MASTER <<== .'.format(x))