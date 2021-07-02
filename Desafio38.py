import emoji
print('=-='*10)
print('''\033[7m          DESAFIO 38          \033[m''')
print('=-='*10)
print('')
print(emoji.emojize(''':bulb: \033[1mEscreva um programa que leia \033[1;35mdois números\033[m\033[1m inteiros e compare-os, mostrando na tela uma mesangem:
\033[1;32m- \033[m\033[1mO \033[1;32mprimeiro valor\033[m é \033[1;35mmaior\033[m
\033[1;32m- \033[m\033[1mO \033[1;32msegundo valor \033[m é \033[1;35mmaior\033[m
\033[1;32m- Não existe\033[m\033[1m valor maior, os dois são \033[1;35miguais\033[m''', use_aliases=True))
print('')
print('\033[7mCOMPARANDO NÚMEROS\033[m')
print('')
n1 = int(input('\033[1mDigite um número inteiro: \033[m'))
n2 = int(input('\033[1mDigite o segundo número:\033[m'))
if n1 > n2:
    print('\033[1mO 1º número é \033[m\033[1;35mMAIOR\033[m')
elif n2 > n1:
    print('\033[1mO 2º número é \033[m\033[1;32mMAIOR\033[m')
else:
    print('\033[1mOs dois valores são \033[m\033[1;31mIGUAIS\033[m')