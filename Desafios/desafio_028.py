from random import randint

numero_magico = randint(0, 5)
num = int(input('Digite um número entre 1 e 5: '))
if numero_magico == num:
    print('PARABÉNS! Você acertou!!')
else:
    print(f'Infelizmente você errou. O número era {numero_magico}. Mais sorte da próxima vez.')
