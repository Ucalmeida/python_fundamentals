nome = str(input('Digite seu nome completo: ')).split()

print(f'O primeiro nome digitado foi: {nome[0].title()}')
print(f'O último nome digitado foi: {nome[len(nome) - 1].title()}')
