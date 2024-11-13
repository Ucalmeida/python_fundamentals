from random import choice

aluno1 = str(input('Digite o nome de um aluno: '))
aluno2 = str(input('Digite o nome de outro aluno: '))
aluno3 = str(input('Digite o nome de outro aluno: '))
aluno4 = str(input('Digite o nome de outro aluno: '))

alunos = [aluno1, aluno2, aluno3, aluno4]
print(f'E o aluno sorteado para limpar o quadro foi: {choice(alunos)}')
