import emoji
from time import sleep
print('=-='*10)
print('''\033[7m          DESAFIO 67          \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mFaça um programa que mostre a \033[m\033[1;32mtabuada \033[m\033[1mde\033[m\033[1;35m vários números\033[m\033[1m, um de cada
vez, para cada valor digitado pelo usuário. O programa será \033[m\033[1;32minterrompido\033[m\033[1m quando o número solicitado for\033[m\033[1;35m negativo\033[m\033[1m.\033[m''', use_aliases=True))
print('')
print('\033[7mTABUADA V3.0\033[m')
print('')

while True:
    n = int(input('\033[1mDigite um número para fazer a tabuada:\033[m '))
    for c in range(1, 11):
        if n < 1:
            break
        s = n * c
        print(f'{n} x {c:2} = {s}')
        sleep(1)
    print('\033[1mPrograma encerrado\033[m')


