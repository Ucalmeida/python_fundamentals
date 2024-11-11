# Lidando com espaçamentos:
nome = input('Qual o seu nome? ')
print(f'Prazer em te conhecer {nome:20}!') # 20 espaços após o valor da variável e antes da última string(Nesse caso, "!")
print(f'Prazer em te conhecer {nome:<20}!') # Alinha o valor da variável a esquerda e dá 20 espaços entre o valor e "!"
print(f'Prazer em te conhecer {nome:>20}!') # Alinha o valor da variável a direita com 20 espaços de diferença entre o valor e a última string(Que nesse caso é um espaço)
print(f'Prazer em te conhecer {nome:^20}!') # Centraliza o valor da variável, usando como valor 20
print(f'Prazer em te conhecer {nome:=^20}!') # Preenche os espaços da variável centralizada com "=", usando como valor base 20

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

# Imprime o primeiro registro e depois o registro seguinte
print(f'A soma é {s}, o produto é {m} e a divisão é {d:.3f}')
print(f'Divisão inteira de {n1} por {n2} é {di} e a potência de {n1} elevado a {n2} é {e}')

# Imprime tudo na mesma linha
print(f'A soma é {s}, o produto é {m} e a divisão é {d:.3f}', end = ' | ') # Posso deixar espaços em branco ou colocar diversos caracteres
print(f'Divisão inteira de {n1} por {n2} é {di} e a potência de {n1} elevado a {n2} é {e}')