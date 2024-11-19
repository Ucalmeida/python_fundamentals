velocidade = int(input('Digite a velocidade de seu veículo: '))
limite_de_velocidade = 80
if velocidade > limite_de_velocidade:
    velocidade_excedente = velocidade - limite_de_velocidade
    multa = velocidade_excedente * 7.00
    print(f'Você excedeu o limite de velocidade. Você foi multado em R${multa:.2f}')
else:
    print('Até aqui tudo bem...')
