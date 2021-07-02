print('=-='*10)
print('''\033[7m          DESAFIO 61          \033[m''')
print('=-='*10)
import emoji
print(emoji.emojize(''':bulb: \033[1mRefaça o \033[m\033[1;32mDESAFIO 051\033[m\033[1m, lendo o \033[m\033[1;35mprimeiro termo\033[m
\033[1me a \033[m\033[1;35mrazão\033[m\033[1m de uma\033[m\033[1;35m PA\033[m\033[1m, mostrando os \033[m\033[1;32m10 primeiros termos\033[m\033[1m da progressão usando a estrutura\033[m\033[1;35m while\033[m\033[1m.\033[m''', use_aliases=True))
print('\033[7mProgressão Aritmética v2.0\033[m')
print('')
primeiro = int(input('Primeiro termo:'))
r = int(input('Razão:'))
term = primeiro
cont = 1
while cont <= 10:
    print(emoji.emojize('{} :arrow_right:'.format(term), use_aliases=True), end='')
    term = term + r
    cont = cont + 1
print('FINISH')


