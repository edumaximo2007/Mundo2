print('=-='*10)
print('''\033[7m          DESAFIO 49          \033[m''')
print('=-='*10)
print('')
import emoji
from time import sleep
print(emoji.emojize(''':bulb: \033[1mRefaça o \033[m\033[1;32mDESAFIO 009\033[m\033[1m, mostrando a \033[m\033[1;35mtabuada\033[m\033[1m de um número que o usúario escolher, só que
agora ultilizando um\033[m\033[1;35m laço for\033[m\033[1m.\033[m''', use_aliases=True))
print('')
print('''\033[7mTABUADA V2.0\033[m''')
print('')
n = int(input('\033[1mDigite um número:\033[m '))
print('')
for c in range(1, 11):
    s = n * c
    sleep(1)
    print('\033[1m{} x {:2} =\033[m \033[1;35m{}\033[m'.format(n, c, s))