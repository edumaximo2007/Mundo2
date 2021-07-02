from random import randint
import emoji
print('=-='*10)
print('''\033[7m          DESAFIO 68          \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mFaça um, programa que jogue \033[m\033[1;35m par ou impar\033[m\033[1m com \no computador. O jogo só será interromppido quando \no jogador \033[m\033[1;32mPERDER\033[m\033[1m, mostrando o total de vitórias consecutivas
que ele conquistou no final do jogo.\033[m''', use_aliases=True))
print('')
print('\033[7mPAR OU IMPAR V2.0\033[m')
print('')
computador = randint(0, 99)
itens = ('Par', 'Impar')
jogada = ('Venceu', 'Perdeu')
par = impar = 0
jogador = 1
while True:
    jogador = int(input('''\033[1mDigite um número\033[m
    \033[1;32m[0]\033[m\033[1;35m PAR\033[m
    \033[1;32m[1]\033[m\033[1;35m IMPAR\033[m\033[1m:\033[m '''))
    if jogador % 2 == 0:
        par += 1
        print(jogador)
    elif computador % 2 == 0:
        print(computador)