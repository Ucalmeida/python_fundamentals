# Condição de existência de um triângulo:
# b + c > a
# a + c > b
# a + b > c

r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceira reta: '))
s1 = r1 + r2
s2 = r1 + r3
s3 = r2 + r3
equilatero = r1 == r2 and r2 == r3
isosceles = r1 == r2 and r2 != r3
escaleno = r1 != r2 and r2 != r3

if s1 > r3 and s2 > r2 and s3 > r1:
    print('Você pode formar um triângulo com essas retas')
    print('É um triângulo Equilátero' if equilatero else 'É um triângulo Escaleno' if escaleno else 'É um triângulo Isósceles')
else:
    print('Essas medidas não atendem à Condição de existência de um triângulo.')
