print('=-='*10)
print('''\033[7m          DESAFIO 46          \033[m''')
print('=-='*10)
import emoji
from time import sleep
print(emoji.emojize(''':bulb: \033[1mFaça um programa que mostre na tela uma\033[m\033[1;35m Contagem regressiva\033[m\033[1m para o estouro
de fogos de artifício, indo de\033[m\033[1;32m 10 até 0\033[m\033[1m, com uma pausa de\033[m\033[1;35m 1 segundo\033[m\033[1m entre elas.\033[m''', use_aliases=True))
print('')
print('''\033[7mCONTAGEM REGRESSIVA\033[m''')
print('')
for c in range(10, -1, -1):
    sleep(1)
    print(c)

print(emoji.emojize(':boom: :collision:', use_aliases=True))