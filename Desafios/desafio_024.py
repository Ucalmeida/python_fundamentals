nome_de_cidade = str(input('Digite o nome de uma cidade: '))
primeiro_nome = nome_de_cidade.split()
if 'SANTO' in primeiro_nome[0].upper():
    print('A cidade digitada começa com SANTO')
else:
    print(f'Cidade digitada: {nome_de_cidade.capitalize()}. Essa cidade não começa com SANTO')
