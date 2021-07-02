print('=-='*10)
print('''\033[7m          DESAFIO 64          \033[m''')
import emoji
print(emoji.emojize(''':bulb: \033[1mCrie um programa que leia\033[m\033[1;35m vários números\033[m\033[1m inteiros
pelo teclado. O programa só vai parar quando o usuário digitar o valor \033[m\033[1;32m99\033[m\033[1m, que é a \033[m\033[1;35m condição de paradaz\033[m\033[1m.
No final, mostre\033[m\033[1;35m quantos números \033[m\033[1mforam digitados e qual foi a \033[m\033[1;35msoma\033[m\033[1m entre eles\033[m\033[1;37m (desconsiderando o flag)\33[m\033[1m.\033[m''', use_aliases=True))
print('')
print('\033[7m TRATANDO VÁRIOS VALORES V1.0\033[m')
print('')
n = 0
soma = 0
cont = 0
soma = int(input('Digite um número:'))
while soma != 999:
    soma = int(input('Digite um número:'))
    n = n + soma
    cont = cont + 1
print('Você digitou {}x, a soma dos valores e = {}'.format(cont, n))
