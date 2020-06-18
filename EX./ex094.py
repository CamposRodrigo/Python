galera= []
pessoa= {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa["Nome"]= str(input('Nome: '))
    while True:
        pessoa["Sexo"]= str(input('Sexo [M/F]:  ')).upper()[0]
        if pessoa["Sexo"]  in 'MF':
            break
        print('Erro!!Por favor digite M ou F .')
    pessoa["Idade"] = int(input('Idade: '))
    soma += pessoa["Idade"]
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar?[S/N]  ')).upper()[0]
        if resp in 'SN':
            break
            print('Erro!!Por favor digite S ou N .')
    if resp == 'N':
        break
print('=-'*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(pessoa)
print(f'B) A media de idade e de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram ==>> ', end='')
for p in galera :
    if p["Sexo"] in 'Ff':
        print(f'{p["Nome"]} - ', end='')
print()
print('D) Lista das pessoas que estao acima da media:')
for p in galera :
    if p["Idade"] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('========================= ENCERRADO =========================')
