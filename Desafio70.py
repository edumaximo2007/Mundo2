import emoji
print('=-='*10)
print('''\033[7m          DESAFIO 70          \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mCrie um programa que leia o \033[m\033[1;35mnome \033[m\033[1me o \033[m\033[1;35mpreço\033[m\033[1m de \033[m\033[1;32mvários produtos\033[m\033[1m. O programa deverá perguntar se o\033[m\033[1;35m usuário\033[m\033[1m vai continuar.
No final, mostre:\033[m

\033[1;32mA)\033[m\033[1m Qual é o\033[m\033[1;35m total gasto\033[m
\033[1;32mB)\033[m\033[1m Quantos produtos custam\033[m\033[1;32m mais\033[m\033[1m de \033[m\033[1;35mR$1000\033[m\033[1m.\033[m
\033[1;32mB)\033[m\033[1m Qual é o \033[m\033[1;35mnome\033[m\033[1m do produto maais\033[m\033[1;32m barato\033[m\033[1m.\033[m''', use_aliases=True))
print('')
print('')