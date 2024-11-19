ano = int(input('Digite um ano: '))
unidade = ano // 1 % 10
dezena = ano // 10 % 10
ano_dezena = str(dezena) + str(unidade)

if ano_dezena != '00' and int(ano_dezena) % 4 == 0:
    print(f'{ano} é Bissexto')
elif ano_dezena == '00' and ano % 400 == 0:
    print(f'{ano} é Bissexto')
else:
    print(f'{ano} não é Bissexto')
