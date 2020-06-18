from datetime import date
n = int(input('Digite o ano do seu nascimento: '))
cal = date.today().year - n
if cal < 18 :
    print('Quem nasceu em {} tem {} anos em {}.'.format(n,cal,date.today().year))
    print('Voce nao se alistou ainda.')
    print('Voce deve se alistar em {}.'.format(n + 18))
    print('Voce fara seu alistamento em {} ano(s).'
          .format((n+18) - date.today().year))
elif cal > 18:
    print('Quem nasceu em {} tem {} anos em {}.'.format(n,cal,date.today().year))
    print('Voce de veria ter se alistado ha {} anos.'.format(cal - 18))
    print('Seu alistamento foi em {}.'.format(n + 18))
else:
    print('Quem nasceu em {} tem {} anos em {} .'.format(n,cal,date.today().year))
    print('Voce tem que se alistar IMEDIATAMENTE!')

