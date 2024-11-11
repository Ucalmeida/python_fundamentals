largura = float(input('Digite a largura de sua parede em metros: '))
altura = float(input('Digite a altura de sua parede em metros: '))
area = largura * altura
quantidade_de_tinta = area / 2

print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area}m².')
print(f'Você vai precisar de {quantidade_de_tinta:.2f}L de tinta para pintar sua parede')
