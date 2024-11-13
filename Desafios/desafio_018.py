from math import radians, sin, cos, tan

angulo = float(input('Digite um ângulo: '))
radianos = radians(angulo)
seno = sin(radianos)
cosseno = cos(radianos)
tangente = tan(radianos)

print(f'Pelo ângulo fornecido, que foi de {angulo} graus, \n'
      f'seu Seno é {seno:.2f}, seu Cosseno é {cosseno:.2f} e sua Tangente é {tangente:.2f}')
