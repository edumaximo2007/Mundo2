import emoji

print('=-=' * 10)
print('''\033[7m          DESAFIO 42          \033[m''')
print(emoji.emojize(''':bulb:\033[1mRefaça o \033[1;32mDESAFIO 035\033[m\033[1m dos triângulos, acrescentando o recurso de mostrar que tipo de 
triângulo será formado:\033[m

\033[1;32m- \033[m\033[1;35mEquilátero\033[m\033[1m: todos os lados iguais\033[m
\033[1;32m- \033[m\033[1;35mIsórceles\033[m\033[1m: dois lados iguais\033[m
\033[1;32m- \033[m\033[1;35mEscaleno\033[m\033[1m: todos os lados diferentes\033[m''', use_aliases=True))
print('')
print('\033[7m TRIÂNGULOS\033[m')
print('')
n = float(input('\033[1mDigite um número A:\033[m '))
o = float(input('\033[1mDigite um número B:\033[m'))
a = float(input('\033[1mDigite um número C:\033[m'))
if n < o + a and o < n + a and a < n + o:
    print('\033[1mOs número acima podem formar um \033[m\033[1;35mTRIÂNGULO \033[m', end='')
    if n == o == a:
        print('\033[1;32mEQUILÁTERO\033[m')
    elif n != o != a != n:
        print('\033[1;32mISÓRCELES\033[m')
    else:
        print('\033[1;32mESCALENO\033[m')
else:
    print('\033[1mOs números acima não podem forma um\033[m\033[1;31m TRIÂNGULO\033[m')



