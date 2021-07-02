import emoji

print('=-='*10)
print('''\033[7m          DESAFIO 50          \033[m''')
print('=-='*10)
print('')
print(emoji.emojize(''':bulb: \033[1mDesenvolva um programa que leia\033[m\033[1;35m seis números inteiros\033[m\033[1m e mostre a soma apenas daqueles que forem \033[m\033[1;32mpares\033[m
\033[1mSe o valor digitado for\033[m\033[1;32m impar\033[m\033[1m, considere-o\033[m''', use_aliases=True))
print('')
print('''\033[7mSOMA DOS PARES\033[m''')
print('')
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}° valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números pares e a soma dele e igual a {}'.format(cont, soma))