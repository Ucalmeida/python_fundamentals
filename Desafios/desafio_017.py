from math import hypot

cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print(f'O valor da hipotenusa para o cateto oposto = {cateto_oposto}\n'
      f'E o cateto adjacente = {cateto_adjacente} é {hipotenusa:.2f}')