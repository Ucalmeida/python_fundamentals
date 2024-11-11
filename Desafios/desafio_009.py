n1 = int(input('Digite um número para exibir sua tabuada: '))

print(f'\nA tabuada de soma de {n1} é:')
for i in range(10):
    print(f'{n1} + {i+1} = {n1 + (i + 1)}')

print(f'\nA tabuada de multiplicação de {n1} é:')
for i in range(10):
    print(f'{n1} x {i+1} = {n1 * (i + 1)}')

print(f'\nA tabuada de subtração de {n1} é:')
for i in range(11):
    print(f'{n1 + i} - {n1} = {(n1 + i) - n1}')

print(f'\nA tabuada de divisão de {n1} é:')
for i in range(10):
    print(f'{n1 + (n1 * i)} : {n1} = {(n1 + (n1 * i)) / n1:.0f}')