num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num1 > num2 > num3:
    print(f'{num1} é o maior número e {num3} é o menor.')
elif num1 > num3 > num2:
    print(f'{num1} é o maior número e {num2} é o menor.')
elif num2 > num1 > num3:
   print(f'{num2} é o maior número e {num3} é o menor.')
elif num2 > num3 > num1:
    print(f'{num2} é o maior número e {num1} é o menor.')
elif num3 > num1 > num2:
    print(f'{num3} é o maior número e {num2} é o menor.')
elif num3 > num2 > num1:
    print(f'{num3} é o maior número e {num1} é o menor.')
