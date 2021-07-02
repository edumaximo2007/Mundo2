print('=-='*10)
print('''\033[7m          DESAFIO 52          \033[m''')
print('=-='*10)
import emoji
print()
print(emoji.emojize(''':bulb: \033[1mFaça um programa que leia um \033[m\033[1;32mnúmero inteiro\033[m\033[1m e diga se 
ele é ou não um\033[m\033[1;35m número primo\033[m\033[1m.\033[m''', use_aliases=True))
print('')
print('\033[7mNÚMEROS PRIMOS\033[m')
print('')
total = 0
núm = int(input('Digite um número: '))
for c in range(1, núm + 1):
    if núm % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\033[1mO número {} foi divisivel {} vezes\033[m'.format(núm, total))
if total == 2:
    print('\033[1mEsse número é\033[m\033[1;32m PRIMO\033[m')
else:
    print('\033[1mEsse número não é\033[m\033[1;31m PRIMO\033[m')
