print('=-='*10)
print('''\033[7m          DESAFIO 48          \033[m''')
print('=-='*10)
print('')
import emoji
print(emoji.emojize(''':bulb: \033[1mFaça um programa que calcule a \033[m\033[1;32msoma\033[m\033[1m entre todos os \033[m\033[1;35mnúmeros impares\033[m
\033[1m que são\033[m\033[1;32m múltiplos de três\033[m\033[1m e que se econtram no intervalo de \033[m\033[1;32m 1\033[m\033[1m até\033[m\033[1;32m 500\033[m\033[1m.\033[m''', use_aliases=True))
print('')
print('''\033[7mSoma ímpares múltiplos de três\033[m''')
print('')
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c  # acumulador
        cont += 1  # Contador
print('\033[1mA soma de todos os {} valores solicitados e {}\033[m'.format(cont, soma))
