import emoji
import datetime
print('=-='*10)
print('''\033[7m          DESAFIO 39          \033[m''')
print('=-='*10)
print('')
print(emoji.emojize('''\033[1m:bulb: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

\033[1m- Se ele\033[1;32m ainda vai se alistar\033[m \033[1mao serviço militar.
\033[1m- Se é a\033[1;32m hora de se alistar.\033[m
\033[1m- Se já\033[1;32m passou do tempo\033[m \033[1mdo alistamento.

Seu programa também deverá mostrar o  tempo que falta ou que passou do prazo.\033[m ''', use_aliases=True))
print('Prcessando a informação...')
print('')
print('\033[7m ALISTAMENTO MILITAR\033[m')
print('')
n = str(input('\033[1mNome completo:\033[m')).strip()
p = int(input('\033[1mInforme o ano de nascimento: \033[m'))
s = str(input('\033[1mInforme seu sexo:\033[m')).strip()
if s == 'Masculino':
    print('\033[1mVocê tem o dever obrigatorio de alistamento.\033[m')
else:
    print('\033[1mVocê não tem o dever obrigatorio de alistamento militar.\033[m')
a = datetime.date.today().year
c = a - p
print('\033[1mQuem nasceu em {} tem {} anos em {}\033[m'.format(p, c, a))
if c == 18:
    print('\033[1m{}, com base nas informações fornecidas você tem {} anos procure um posto militar mais próximo para fazer o alistamento.\033[m'.format(n, c))
elif c <= 18:
    b = 18 - c
    print('\033[1m{}, com base nas iformações fornecidas você tem {} anos ainda falta {} anos para o alistamento obrigatorio.\033[m'.format(n, c, b))
    m = a + b
    print('\033[1mSeu alistamento será em {}.\033[m'.format(m))
else:
    b = c - 18
    print('\033[1m{}, com base nas informações fornecidas você tem {} anos, passou {} anos do prazo para o alistamento militar, procure um posto para mais informações.\033[m'.format(n, c, b))
    m = a - b
    print('\033[mSeu alistamento foi em {}.\033[m'.format(n, m))
print('\033[1;32mBrasil acima de tudo, Deus acima de todos\033[m')
