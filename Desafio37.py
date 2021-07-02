import emoji
print('=-='*10)
print('''\033[7m          DESAFIO 37          \033[m''')
print('=-='*10)
print('')
print(emoji.emojize(''':bulb:\033[1mEscreva um programa que leia um número inteiro qualquer e peça para o
 usuário escolher qual será a \033[1;35mbase de conversão\033[m:
 \033[1;32m- \033[m\033[1;35m1\033[m para\033[1;32m binário\033[m
 \033[1;32m- \033[m\033[1;35m2\033[m para\033[1;32m octal\033[m
 \033[1;32m- \033[m\033[1;35m3\033[m para\033[1;32m hexadecimal\033[m''', use_aliases=True))
print('')
print('\033[7m CONVERSOR DE BASES NÚMERICAS\033[m')
print('')
num = int(input('\033[1mDigite um número inteiro:\033[m '))
print('''\033[1mEscolha uma opção para conversão:
[1] converter para \033[m\033[1;34mBINÁRIO\033[m
\033[1m[2] converter para \033[m\033[1;34mOCTAL\033[m
\033[1m[3] converter para \033[m\033[1;34mHEXADECIMAL\033[m''')
opção = int(input('\033[1mSua opção:\033[m'))
if opção == 1:
    print('\033[1m{} convertido para\033m\033[1;34m BINÁRIO\033[m\033[1m, é igual a {}\033[m'.format(num, bin(num)[2:]))
elif opção == 2:
    print('\033[1m{} convertido para\033[m\033[1;34m OCTAL\033[m\033[1m, é igual a {}\033[m'.format(num, oct(num)[2:]))
elif opção == 3:
    print('\033[1m{} convertido para \033[m\033[1;34m HEXADECIMAL\033[m\033[1m, é igual a {}\033[m'.format(num, hex(num)[2:]))
else:
    print('\033[1mOpção invalida, tente novamente\033[m')