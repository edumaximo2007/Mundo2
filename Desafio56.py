print('=-='*10)
print('''\033[7m          DESAFIO 56          \033[m''')
print('=-='*10)
import emoji
print(emoji.emojize(''':bulb: \033[1mDesenvola um programa que leia o \033[m\033[1;32mnome\033[m\033[1m, \033[m\033[1;32midade\033[m\033[1m e \033[m\033[1;32msexo\033[m
\033[1mde\033[m \033[1;35m4 pessoas\033[m\033[1m. No final do programa, mostre:\033[m

\033[1;32m:arrow_forward: \033[m\033[1mA\033[m\033[1;35m média de idade\033[m\033[1m do grupo.\033[m
\33[1;32m:arrow_forward: \033[m\033[1mQual é o nome do homem\033[m\033[1;35m mais velho\033[m\033[1m.\033[m
\033[1;32m:arrow_forward: \033[m\033[1mQuantas mulheres têm\033[m\033[1;35m menos de 20\033[m\033[1m anos.\033[m''', use_aliases=True))
print('')
print('\033[7mANALISADOR COMPLETO\033[m')
print('')

maiorh = 0
hvelho = ''
mulher20 = 0
for p in range(1, 5):
    print(f'\033[1m=-=-=-=-=- {p}º Pessoa -=-=-=-=-=-=-=\033[m',)
    n = str(input('Nome: ')).strip()
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: '))
    c = i / p
    if p == 1 and s in 'Mm':
        hvelho = n
    if s in 'Mm' and i > maiorh:
        maiorh = i
        hvelho = n
    if s in 'Ff' and i < 20:
        mulher20 += 1
print('=-='*20)
print('\033[1mA média de idade do grupo é {:.2f}'.format(c))
print('{} e o homem mais velho do grupo e tem {} anos'.format(hvelho, maiorh))
print('Existe {} mulheres com menos de 20 anos\033[m'.format(mulher20))
