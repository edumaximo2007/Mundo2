import emoji
print('=-='*10)
print('''\033[7m          DESAFIO 51          \033[m''')
print('=-='*10)
print('')
print(emoji.emojize(''':bulb: \033[1mDesenvola um programa que leia o \033[m\033[1;35mprimeiro termo\033[m\033[1m e a\033[m\033[1;35m razão\033[m\033[1m de uma \033[m\033[1;32mPA\033[m\033[1m.
No final, mostre os\033[m\033[1;32m 10\033[m\033[1m primeiros termos dessa progressão\033[m''', use_aliases=True))
print('')
print('\033[7mPROGRESSÃO ARITIMÉTICA\033[m')
print('')
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{}'.format(c), end=' ')