nome = str(input('Digite seu nome completo: '))
upper = nome.upper()
lower = nome.lower()
contagem_de_letras = len(nome)
divisao = nome.split()
juncao_sem_espacos = ''.join(divisao)
contagem_sem_espacos = len(juncao_sem_espacos)
contagem_do_primeiro_nome = len(divisao[0])

print(f'Todas as letras maiúsculas: {upper}')
print(f'Todas as letras minúsculas: {lower}')
print(f'Tamanho do nome com espaços: {contagem_de_letras}')
print(f'Tamanho do nome sem espaços: {contagem_sem_espacos}')
print(f'Tamanho do primeiro nome: {contagem_do_primeiro_nome}')