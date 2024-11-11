n = bool(input('Digite um valor: '))
print(n) # Se digitei um valor, exibe True. Se não digitei nada, exibe False

m = input('Digite algo: ')
print(f'É um inteiro? {m.isnumeric()}') # Verifica se o que foi digitado pode ser convertível em inteiro
print(f'É apenas letras? {m.isalpha()}') # Verifica se é apenas letra
print(f'É letras ou números? Ou ambos? {m.isalnum()}') # Verifica se é letra ou número, ou ambos. Se pressionar espaço, é False