import math
import random

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz de {num} é aproximadamente {raiz:.2f} - Exibindo dois números após o ponto')
print(f'A raiz de {num} é aproximadamente {math.ceil(raiz)} - Arredondado para cima')
print(f'A raiz de {num} é aproximadamente {math.floor(raiz)} - Arredondado para baixo')
print(f'A porção inteira da raiz de {num} é {math.trunc(raiz)}')

num2 = random.randint(1, 10)
num3 =  random.random()
print(f'Número randômico entre 1 e 10: {num2}')
print(f'Número randômico: {num3:.2f}')
