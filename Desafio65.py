import emoji
print('=-='*10)
print('''\033[7m          DESAFIO 65          \033[m''')
print('=-='*10)
print(emoji.emojize(''':bulb: \033[1mCrie um programa que leia \033[m\033[1;35mvários números \033[m\033[1minteiros pelo teclado. No final da execução, mostre a \033[m\033[1;32mmédia entre todos\033[m
\033[1mos valores a qual foi o\033[m\033[1;32m maior\033[m\033[1m e o\033[m\033[1;32m menor\033[m\033[1m valores lidos. O
programa deve perguntar ao usuário se ele quer ou não\033[m\033[1;35m continuar\033[m\033[1m a digitar valores\033[m
''', use_aliases=True))
print('')
print('\033[7mMAIOR E MENOR VALOR\033[m')
print('')
p = 'S'
cont = v = n1 = maior = menor = 0

while p == 'S':
    n = int(input('\033[1mDigite um número: \033[m'))
    v += n
    cont += 1
    n1 = v / cont
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    p = str(input('\033[1mDeseja continuar \033[1;32m[S/N]\033[m\033[1m:\033[m ')).strip()[0].upper()
print('\033[1mVocê digitou {}x a média entre os valores é {}\033[m'.format(cont, n1))
print('\033[1mO número maior é o {} e o menor número e o {}\033[m'.format(maior, menor))
