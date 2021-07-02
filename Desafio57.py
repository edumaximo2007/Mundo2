print('=-='*10)
print('''\033[7m         DESAFIO 57          \033[m''')
print('=-='*10)
print('')
import emoji
print(emoji.emojize(''':bulb: \033[1mFaça um programa que leia o \033[m\033[1;32msexo\033[m\033[1m de uma pessoa, mas só aceite os valores \033[m\033[1;35m'M'\033[m\033[1m ou \033[m\033[1;35m'F'\033[m.
\033[1mCaso esteja errado, peça a digitação novamente até ter um valor correto.\033[m''', use_aliases=True))
print('')
print('\033[7mVALIDAÇÃO DE DADOS\033[m')
print('')

n = str(input('Sexo: ')).strip().upper()[0]
while n not in 'MmFf':
    if n == 'Ff' in 'Mf':
        print('Dados correto')
    else:
        print('Opção inválida tente novamente')
    n = str(input('Sexo:')).strip().upper()[0]