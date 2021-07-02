import emoji
print('=-='*10)
print('''\033[7m          DESAFIO 63          \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mEscreva um programa que leia um \033[m\033[1;35mnúmero\033[m\033[1;32m n \033[m\033[1minteiro qualquer e mostre na tela os\033[m\033[1;32m n \033[m\033[1m primeiros elementos de uma\033[m
\033[1;32mSequência de Fibonacci\033[m\033[1m.\033[m

\033[1;37mEx:\033[m
\033[1;32m0 :arrow_right: 1 :arrow_right: 1 :arrow_right: 2 :arrow_right: 3 :arrow_right: 5 :arrow_right: 8\033[m''', use_aliases=True))
print('')
print('\033[7m SEQUÊNCIA DE FIBONACCI\033[m')
print('')
n = int(input('Digite um número: '))
n1 = 0
n2 = 1
print(emoji.emojize('{} :arrow_right: {}'.format(n1, n2), use_aliases=True), end='')
cont = 3
while cont <= n:
    n3 = n1 + n2
    print(emoji.emojize(':arrow_right: {}'.format(n3), use_aliases=True), end=' ')
    n1 = n2
    n2 = n3
    cont = cont + 1
print('FINISH')
