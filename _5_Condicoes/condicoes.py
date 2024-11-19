tempo = int(input('Quantos anos tem seu carro? '))

# if tempo ≤ 3:
#     print('Carro novo')
# else:
#     print('Carro velho')

# Forma mais simplificada
print('Carro novo' if tempo <= 3 else 'Carro veho')

print('--FIM--')

nome = str(input('Qual é o seu nome? '))
if nome == 'Urian':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão ordinário...')
print(f'Bom dia {nome}!')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'A sua média foi {media:.1f}')

if media >= 7.0:
    print(f'Sua média foi boa! Muito Bem!')
else:
    print(f'Sua média foi ruim. Vá estudar e pare de ver instagram!!')
