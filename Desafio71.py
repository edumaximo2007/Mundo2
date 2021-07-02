import emoji
print('=-='*10)
print('''\033[7m          DESAFIO 71          \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mCrie um programa que simule o funcionamento de um\033[m\033[1;32m caixa eletrônico\033[m\033[1m. No início, pergunte ao usuário
qual será o \033[m\033[1;35mvalor a ser sacado\033[m\033[1m(número inteiro) e o programa vai informa quantas\033[m\033[1;35m cédulas\033[m\033[1m de valor serão entregues\033[m

\033[1;32mOBS:\033[m\033[1m Considere que o caixa possui cédulas de \033[m\033[1;35mR$50\033[m\033[1m,\033[m\033[1;35m R$20\033[m\033[1m,\033[m\033[1;35m R$10\033[m\033[1m e\033[m\033[1;35m R$1\033[m\033[1m.\033[m''', use_aliases=True))
