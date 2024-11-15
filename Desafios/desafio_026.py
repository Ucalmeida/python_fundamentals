frase = str(input('Digite uma frase: ')).lower().strip()
incidencia_da_letra_a = frase.count('a')
primeira_incidencia = frase.find('a') + 1
ultima_incidencia = frase.rfind('a') + 1

print(f'Quantas vezes a letra "A" aparece: {incidencia_da_letra_a}')
print(f'Posição da primeira Incidência da letra "A": {primeira_incidencia}')
print(f'Posição da última Incidência da letra "A": {ultima_incidencia}')
