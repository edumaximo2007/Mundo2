print('=-='*10)
print('''\033[7m          DESAFIO 54          \033[m''')
print('=-='*10)
import emoji
print(emoji.emojize(''':bulb: \033[1m Crie um programa que leia o \033[m\033[1;32mano de nascimento\033[m
\033[1m de\033[m \033[1;35m sete pessoas\033[m\033[1m. No final, mostre quantas pessoas ainda não atigiram
a maioridade e quantas já são maiores.\033[m''', use_aliases=True))
print('')
print('\033[7mGRUPO DA MAIORIDADE\033[m')
print('')
from datetime import date
at = date.today().year
tmaior = 0
tmen = 0
for c in range(1, 8):
    n = str(input('{}° nome: '.format(c))).strip()
    a = int(input('Ano de nascimento: '))
    s = at - a
    if s >= 21:
        tmaior += 1
    else:
        tmen += 1
print('\033[1m{} totalizam maioridade\033[m'.format(tmaior))
print('\033[1m{} totallizam menor idade\033[m'.format(tmen))
