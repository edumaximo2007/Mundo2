from random import randint
import emoji
from time import sleep
print('=-='*10)
print('''\033[7m          DESAFIO 45          \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mCrie um programa que faça o computador jogar\033[m\033[1;32m Jokenpô\033[m\033[1m com você\033[m

:fist: :hand: :v:''', use_aliases=True))
print('')
print('\033[7m      JOKENPÔ     \033[m')
print('')
itens = (':fist:', ':hand:', ':v:')
computador = randint(0, 2)
print(emoji.emojize('''\033[1mOpções:\033[m
\033[1;32m-\033[m\033[1m[\033[m\033[1;31m0\033[m\033[1m]\033[m:fist:
\033[1;32m-\033[m\033[1m[\033[m\033[1;31m1\033[m\033[1m]\033[m:hand:
\033[1;32m-\033[m\033[1m[\033[m\033[1;31m2\033[m\033[1m]\033[m:v:''', use_aliases=True))
jogador = int(input('\033[1mEscolha uma opção:\033[m'))
print('\33[1mProcessando informação....\033[m')
sleep(1)
print('\033[7mJO\033[m')
sleep(1)
print('\033[7mKEN\033[m')
sleep(1)
print('''\033[7mPÔ  \033[m''')
print('-='*9)
print(emoji.emojize('\033[1mComputador jogou\033[m\033[31m {}\033[m'.format(itens[computador]), use_aliases=True))
print(emoji.emojize('\033[1mJogador jogou\033[m\033[35m {}\033[m'.format(itens[jogador]), use_aliases=True))
print('-='*9)
if computador == 0: #Computador jogou PEDRA
    if jogador == 0:
        print('\033[1mEmpate\033[m')
    elif jogador == 1:
        print('\033[1mJogador\033[m\033[1;32m venceu\033[m')
    elif jogador == 2:
        print('\033[1;31mComputador venceu\033[m')
    else:
        print('\033[1mJogada inválida\033[m')
elif computador == 1: #Computardor jogou PAPEL
    if jogador == 0:
        print('\033[1;31mComputador venceu\033[m')
    elif jogador == 1:
        print('\033[1mEmpate\033[m')
    elif jogador == 2:
        print('\033[1mJogador\033[m\033[1;32m venceu\033[m')
    else:
        print('\033[1mJogada inválida\033[m')
elif computador == 2: #Computador jogou TESOURA
    if jogador == 0:
        print('\033[1mJogador\033[m\033[1;32m venceu\033[m')
    elif jogador == 1:
        print('\033[1;31mComputador venceu\033[m')
    elif jogador == 2:
        print('\033[1mEmpate\033[m')
    else:
        print('\033[1mJogada inválida\033[m')
else:
    print('\033[1mJogada inválida, tente novamente!!\033[m')

