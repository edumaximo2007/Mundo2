print('=-='*10)
print('''\033[7m          DESAFIO 60          \033[m''')
print('=-='*10)
import emoji
print(emoji.emojize(''':bulb: \033[1mFaça um programa que leia um \033[m\033[1;35mnúmero\033[m
\033[1mqualquer e mostre o seu \033[m\033[1;32mfatorial\033[m\033[1m.\033[m

\033[1;37mEx:\033[m
\033[1;35m5!\033[m\033[1;37m = 5 x 4 x 3 x 2 x 1 = \033[m\033[1;32m120\033[m''', use_aliases=True))
print('')
print('\033[7mCALCULO FATORIAL\033[m')
print('')
n = int(input('Digite um número: '))
f = 1
c = n
print('Calculando {}! = '. format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print('{}'.format(f))