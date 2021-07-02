from random import randint
from time import sleep
print('=-='*10)
print('''\033[7m          DESAFIO 58          \033[m''')
print('=-='*10)
import emoji
print(emoji.emojize(''':bulb: \033[1mMelhore o jogo do \033[m\033[1;32mDESAFIO 028 \033[m\033[1monde o computador vai "pensar" e um\033[m
\033[1;35m número entre 0 e 10\033[m\033[1m. Só que agora o jogador vai tentar adivinha até acertar, mostrando no final
quantos palpites foram necessários para vencer.\033[m''', use_aliases=True))
print('')
print('\033[7mJOGO DA ADIVINHAÇÃO V1.0\033[m')
print('')
chance = 0
c = randint(0, 10)
print('\033[1mTente adivinhar qual número estou pensando de 0 à 10...\033[m')
tent = 0
genio = False
while not genio:
    j = int(input('Digite um número:'))
    tent += 1
    if j == c:
        genio = True
    else:
        if j < c:
            print('Tente novamente com um número maior')
        elif j > c:
            print('tente novamente com um número menor')
print('Acertou com {} tentativas, inseto'.format(tent))