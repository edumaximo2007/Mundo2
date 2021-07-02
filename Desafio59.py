from time import sleep
print('=-='*10)
print('''\033[7m          DESAFIO 59          \033[m''')
print('=-='*10)
import emoji
print(emoji.emojize(''':bulb: \033[1mCrie um programa que leia\033[m\033[1;32m dois valores\033[m\033[1m e mostre um \033[m\033[1;35mmenu\033[m\033[1m na tela:\033[m

\033[1;32m[1]\033[m\033[1;35m somar\033[m
\033[1;32m[2]\033[m\033[1;35m multiplicar\033[m
\033[1;32m[3]\033[m\033[1;35m maior\033[m
\033[1;32m[4]\033[m\033[1;35m novos números\033[m
\033[1;32m[5]\033[m\033[1;35m sair do programa\033[m

\033[1mSeu programa deverá realizar a operação solicitada em cada caso.\033[m''', use_aliases=True))
print('')
print('\033[7mMENU DE OPÇÕES\033[m')
print('')
n = int(input('\033[1mDigite o 1° número:\033[m '))
n1 = int(input('\033[1mDigite o 2° número:\033[m '))
op = 0
while op != 5:
    print('=-='*6)
    print('''\033[1m    [\033[1;32m1\033[m\033[1m]\033[m\033[1;35m SOMAR\033[m
    \033[1m[\033[m\033[1;32m2\033[m\033[1m\033[1m]\033[m\033[1;35m MULPLICAR\033[m
    \033[1m[\033[m\033[1;32m3\033[m\033[1m\033[1m]\033[m\033[1;35m MAIOR\033[m
    \033[1m[\033[m\033[1;32m4\033[m\033[1m\033[1m]\033[m\033[1;35m NOVOS NÚMEROS\033[m
    \033[1m[\033[m\033[1;32m5\033[m\033[1m\033[1m]\033[m\033[1;35m SAIR\033[m''')
    op = int(input('\033[1m    Digite uma opção:\033[m '))
    print('=-='*6)
    if op == 1:
        s = n + n1
        print('\033[1m{} + {} = {}\033[m'.format(n, n1, s))
        sleep(1)
    elif op == 2:
        x = n * n1
        print('\033[1m{} x {} = {}\033[m'.format(n, n1, x))
        sleep(1)
    elif op == 3:
        if n > n1:
            print('\033[1m{} e maior que {}\033[m'. format(n, n1))
            sleep(1)
        else:
            n1 < n
            print('\033[1m{} e maior que {}\033[m'.format(n1, n))
    elif op == 4:
        n = int(input('\033[1mDigite o 1° número:\033[m '))
        n1 = int(input('\033[1mDigite o 2° número:\033[m '))
    elif op == 5:
        print('\033[1mSair\033[m')
    else:
        print('\033[1;31mOpção invalida, tente novamente\033[m')
        sleep(1)
sleep(2)
print('\033[1mFechando aplicação\033[m')




