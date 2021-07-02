import emoji
print('=-='*10)
print('''\033[7m          DESAFIO 40          \033[m''')
print('=-='*10)
print('')
print(emoji.emojize(''':bulb:\033[1m Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final
de acordo com a média antingida:\033[m

\033[1;32m-\033[m \033[1mMédia abaixo de \033[1;32m5.0\033[m:
\033[1;35m REPROVADO\033[m
\033[1;32m-\033[m \033[1mMédia entre \033[1;32m5.0\033[m \033[1me\033[m \033[1;32m6.9\033[m:
\033[1;35m RECUPERAÇÃO\033[m
\033[1;32m-\033[m \033[1mMédia \033[1;32m7.0\033[m \033[1mou superior :\033[m
\033[1;35m APROVADO\033[m''', use_aliases=True))
print('')
print('\033[7m MÉDIA ALUNO\033[m')
print('')
print('\033[1mPreencha o formulario abaixo\033[m')
n = str(input('\033[1mNome completo:\033[m'))
m1 = float(input('\033[1mNota 1ª avaliação:\033[m '))
m2 = float(input('\033[1mNota 2ª avaliação:\033[m '))
nota = (m1 + m2) /2
if nota >= 7.0:
    print('\033[1mParabéns {} você foi aprovado sua média ficou\033[m\033[1;34m {:.1f}\033[m'.format(n, nota))
elif nota >= 5.0 and nota < 7:
    print('\033[1m{} você ficou em recuperação sua media ficou\033[m\033[1;31m {:.1f}\033[m\033[1m estude mais.\033[m'.format(n, nota))
elif nota <= 5:
    print('\033[1m{}, você foi reprovado você não atingiu a média, sua média é \033[m\033[1;31m{:.1f}\033[m.'.format(n, nota))
