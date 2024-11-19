salario = float(input('Digite o salário do funcionário: '))
if salario > 1250.0:
    salario += (salario * 10) / 100
    print(f'Seu salário ficou em R${salario:.2f}')
else:
    salario += (salario * 15) / 100
    print(f'Seu salário ficou em R${salario:.2f}')
