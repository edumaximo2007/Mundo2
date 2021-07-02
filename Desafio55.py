print('=-='*10)
print('''\033[7m          DESAFIO 55          \033[m''')
print('=-='*10)
import emoji
print(emoji.emojize(''':bulb: \033[1mFaça um programa que leia o \033[m\033[1;32mpeso\033[m
\033[1mde\033[m \033[1;35mcinco pessoas\033[m\033[1m. No final, mostre qual foi\033[m\033[1;32m maior\033[m \033[1me o\033[m \033[1;32m menor\033[m
\033[1mpeso lidos.\033[m''', use_aliases=True))
print('')
print('\033[7mDESAFIO 55\033[m')
print('')
pema= 0
peme = 0
for c in range(1, 6):
    n = float(input('\033[1m{}° digite seu peso:\033[m '.format(c)))
    if c == 1:
        pema = n
        peme = n
    else:
        if n > pema:
            pema = n
        if n < peme:
            peme = n
print('O maior peso lido e {}Kg'.format(pema))
print('O menor peso lido e {}Kg'.format(peme))
