distancia = int(input('Qual a distância que você vai viajar em Km? '))

if distancia <= 200:
    custo = distancia * 0.50
    print(f'O valor de sua passagem ficou em R${custo:.2f}')
else:
    custo = distancia * 0.45
    print(f'O valor de sua passagem ficou em R${custo:.2f}')
