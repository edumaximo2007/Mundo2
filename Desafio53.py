print('=-='*10)
print('''\033[7m          DESAFIO 53          \033[m''')
print('=-='*10)
print('')
import emoji
print(emoji.emojize(''':bulb: \033[1mCrie um programa que leia uma\033[m\033[1;32m frase\033[m\033[1m e diga se 
ela é um \033[m\033[1;35mpalídromo\033[m\033[1m, desconsiderando os espaços.

Ex:\033[m
\033[1;31mAPOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTORAM A DATA DA MARATONA\033[m''', use_aliases=True))
print('')
print('\033[7mPALINDRÓMO\033[m')
print('')
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
#inverso = junto '[: : -1]'COM FATIAMENTO
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('\033[1mTemos um \033[m\033[1;35mPALÍNDROMO\033[m')
else:
    print('\033[1mA frase digitada\033[m\033[1;31m NÂO\033[m\033[1m é um\033[m\033[1;35m palíndromo\033[m')
