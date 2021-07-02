import emoji
from datetime import date
print('=-='*10)
print('''\033[7m          DESAFIO 69          \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mCrie um programa que leia a \033[m\033[1;35midade\033[m\033[1m e o \033[m\033[1;35msexo\033[m\033[1m de \033[m\033[1;32mvárias pessoas\033[m\033[1m. A cada pessoa cadastrada, o programa deverá perguntar se o\033[m\033[1;35m usuário\033[m\033[1m quer ou não continuar.
No final, mostre:\033[m

\033[1;32mA)\033[m\033[1m Quantas pessoas tem mais de \033[m\033[1;35m18 anos\033[m\033[1m.\033[m
\033[1;32mB)\033[m\033[1m Quantos\033[m\033[1;32m homens\033[m\033[1m foram cadastrados.\033[m
\033[1;32mC)\033[m\033[1m Quantas\033[m\033[1;32m mulheres\033[m\033[1m tem menos de \033[m\033[1;35m 20 anos\033[m\033[1m.\033[m''', use_aliases=True))
print('')
print('\033[7mEstatisticas V2.0\033[m')
print('')
atual = date.today().year
homem = mulher = menor = idade = 0
while True:

