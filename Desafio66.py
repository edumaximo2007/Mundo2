import emoji
print('=-='*10)
print('''\033[7m          DESAFIO 66          \033[m''')
print('=-='*10)
print('')
print(emoji.emojize(''':bulb: \033[1mCrie um programa que leia \033[m\033[1;35mvários números\033[m\033[1m inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor\033[m\033[1;32m 999\033[m\033[1m, que é a \033[m\033[1;35mcondição de parada\033[m\033[1m. No final, mostre\033[m\033[1;35m quantos números\033[m\033[1m foram digitados
e qual foi a \033[m\033[1;35msoma\033[m\033[1m entre eles\033[m\033[1;37m(desconsiderando o flag).\033[m''', use_aliases=True))
print('')
print('\033[7mVÁ´RIOS NÚMEROS COM FLAG\033[m')
print('')
cont = 0
soma = 0
n = 0
while True:
    n = int(input('\033[1mDigite um número:\033[m'))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'\033[1mVocê digitou \033[m\033[1;32m{cont}x\033[m\033[1m e a soma entre eles é \033[m\033[1;35m{soma}\033[m')