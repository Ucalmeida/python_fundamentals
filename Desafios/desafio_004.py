valor = input('Digite alguma coisa: ')
print('')
print(f'O tipo primitivo de {valor} é {type(valor)}')
if valor.isspace():
    print(f'{valor} só tem espaços')
else:
    print(f'{valor} não tem só espaços')

if valor.isnumeric():
    print(f'{valor} é um número')
else:
    print(f'{valor} não é um número')

if valor.isalpha():
    print(f'{valor} é alfabético')
else:
    print(f'{valor} não é alfabético')

if valor.isalnum():
    print(f'{valor} é alfanumérico')
else:
    print(f'{valor} não é alfanumérico')

if valor.isupper():
    print(f'{valor} está em maiúsculas')
else:
    print(f'{valor} não está em maiúsculas')

if valor.islower():
    print(f'{valor} está em minúsculas')
else:
    print(f'{valor} não está em minúsculas')

if valor.istitle():
    print(f'{valor} está capitalizada')
else:
    print(f'{valor} não está capitalizada')
