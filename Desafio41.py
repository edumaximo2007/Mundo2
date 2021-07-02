import emoji
import datetime
print('=-='*10)
print('''\033[7m          DESAFIO 41          \033[m''')
print('=-='*10)
print('')
print(emoji.emojize(''':bulb:\033[1m A Conferedação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
sua categoria, de acordo com a idade:\033[m

\033[1;32m-\033[m\033[1m Até\033[m\033[1;32m 9 anos\033[m\033[1m:\033[m\033[1;35mMIRIM\033[m
\033[1;32m-\033[m\033[1m Até\033[m\033[1;32m 14 anos\033[m\033[1m:\033[m\033[1;35mINFANTIL\033[m
\033[1;32m-\033[m\033[1m Até\033[m\033[1;32m 19 anos\033[m\033[1m:\033[m\033[1;35mJUNIOR\033[m
\033[1;32m-\033[m\033[1m Até\033[m\033[1;32m 20 anos\033[m\033[1m:\033[m\033[1;35mSÊNIOR\033[m
\033[1;32m-\033[m\033[1m Acima:\033[m\033[1;35mMASTER\033[m''', use_aliases=True))
print('')
print('\033[7mCLASSIFICANDO ATLETAS\033[m')
print('')
a = int(input('\033[1mDigite o ano para analisar a categoria: \033[m'))
print('')
#Ano atual\ ano nascimento calc
d = datetime.date.today().year
c = d - a
if c <= 9:
    print('\033[1mEsse nadador pertecente a categoria \033[m\033[1;35mMIRIM\033[m\033[1m ele tem {} anos.\033[m'.format(c))
elif c <= 14:
    print('\033[1mEsse nadador pertence a categoria\033[m\033[1;35m INFANTIL\033[m\033[1m ele tem {} anos.\033[m'.format(c))
elif c <= 19:
    print('\033[1mEsse nadador pertence a categoria \033[m\033[1;35mJUNIOR\033[m\033[1m, ele tem {} anos.\033[m'.format(c))
elif c <= 20:
    print('\033[1mEsse nadador pertence a categoria \033[m\033[1;35mSENIOR\033[m\033[1m, ele tem {} anos.\033[m'.format(c))
elif c >= 21:
    print('\033[1mEsse nadador pertence a categoria\033[m\033[1;35m MASTER\033[m\033[1m, ele tem {} anos.\033[m'.format(c))