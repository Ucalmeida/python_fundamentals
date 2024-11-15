### Fatiamento ###
frase = 'Curso em Video Python'
print(frase[9]) # Maneira mais simples de fatiar

# Isso significa: Vai do 9 ao 13, incluindo o 9 e excluindo o 13
print(frase[9:13]) # Fatia de 9 ao 12 - Para de contar no 13(Fica de fora)

# Significa: Vai do 9 ao 21, incluindo o 9 e excluindo o 21
print(frase[9:21])

# Significa: Vai do 9 ao 21, a cada 2, incluindo o 9 e excluindo o 21
print(frase[9:21:2])

# Significa: Vai do início ao 5, incluindo o 0 e excluindo o 5
print(frase[:5]) # Imprime: Curso

#Significa: Vai do 15 ao final
print(frase[15:]) # Imprime: Python

# Significa: Vai do 9 ao final, pulando a cada 3
print(frase[9::3])

### Análise ###
# Comprimento
print(len(frase))

# Count: Conta quantas vezes existe a letra 'o'
print(frase.count('o'))

# Significa: Contar a ocorrência do caractere 'o'
# do 0 ao 13, incluindo o 0 e excluindo o 13
print(frase.count('o', 0, 13))

# Quantas vezes encontrou 'deo'
print(frase.find('deo')) # Indica onde começou o 'deo' - No caso, na posição 11

# Quando coloca uma string que não existe, retorna -1(Não encontrado)
print(frase.find('Android'))

# Verifica se existe a palavra Curso em frase: Retorna True
print('Curso' in frase)

### Transformação ###
# Replace
android = frase.replace('Python', 'Android') # Faz o replace e precisa adicionar a uma nova variável
print(android) # Essa variável exibe Android no lugar de Python
print(frase) # Mas a variável original não foi alterada, permanecendo com o valor Python

# Upper - Maiúsculas
print(frase.upper())

# Lower - Minúsculas
print(frase.lower())

# Capitalize - Deixa todas as letras minúsculas, menos a primeira, que fica maiúscula
print(frase.capitalize())

# Title
title = frase.lower() # Transformo todas as letras em minúsculas e atribuo a variável title
print(title.title()) # O title deixa a primeira letra de cada palavra dentro da frase como maiúscula

# Strip
frase = '   Aprenda Python  '
print(frase.strip()) # Remove todos os espaços inúteis
print(frase.rstrip()) # Remove todos os espaços inúteis do lado direito
print(frase.lstrip()) # Remove todos os espaços inúteis do lado esquerdo

### Divisão ###
# Split: Divide uma string em uma lista
print(frase.split()) # Fica ['Aprenda',  'Python']

### Junção ###
# Join: Une uma lista conforme o caractere fornecido.
# Nesse caso, ['Aprenda', 'Python'] fica Aprenda-Python
print('-'.join(frase.split()))
