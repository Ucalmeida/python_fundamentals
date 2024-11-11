dias = int(input('Quantos dias alugados? '))
kilometros = float(input('Quantos Km rodados? '))
custo = (dias * 60.0) + (kilometros * 0.15)

print(f'O valor a pagar pelo aluguel do veículo, \npor '
      f'{dias} dias e {kilometros}Km rodados é '
      f'R${custo:.2f}')
