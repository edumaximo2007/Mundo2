import emoji

print('=-=' * 10)
print('''\033[7m          DESAFIO 44          \033[m''')
print('=-=' * 10)
print('')
print(emoji.emojize(''':bulb:\033[1m Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu\033[m\033[1;32m preço normal\033[m\033[1m e\033[m\033[1;32m condição de pagamento\033[m\033[1m:\033[m

\033[1;32m-\033[m\033[1m À vista\033[m\033[1;35m dinheiro cheque\033[m\033[1m:\033[m\033[1;32m 10%\033[m\033[1m de desconto\033[m
\033[1;32m-\033[m\033[1m À vista no\033[m\033[1;35m cartão\033[m\033[1m:\033[m\033[1;32m 5%\033[m\033[1m de desconto\033[m
\033[1;32m-\033[m\033[1m Em até\033[1;35m 2x no cartão\033[m\033[1m: preço normal\033[m
\033[1;32m-\033[m\033[1;35m 3x ou mais\033[m\033[1m no cartão:\033[m\033[1;32m 20%\033[m\033[1m de juros\033[m''',
                    use_aliases=True))
print('')
print('\033[7m GEGERENCIADOR DE PAGAMENTO \033[m')
print('')
p = float(input('\033[1mDigite o valor do produto:\033[m '))
b = str(input('\033[1mInforme a forma de pagamento:\033[m'))
a = p - (p * 10 / 100)
ca = p - (p * 5 / 100)

if b == 'Dinheiro' or b == 'Cheque' or b == 'Debito':
    print('\033[1mÀ vista no {}, com 10% de desconto R${:.2f}\033[m'.format(b,a))
else:
    if b == 'Crédito':
        t = str(input('\033[1mÀ vista ou parcelado?\033[m '))
        if t == 'À vista':
            print('\033[1mÀ vista no {}, com 5% de desconto {:.2f}'.format(b, ca))
        else:
            if t == 'Parcelado':
                d = int(input('\033[1mNúmero de parcelas:\033[m'))
                if d == '2':
                   print('\033[1mR${:.2f } em {}x sem juros no cartão, parcelas de R${:.2f}\033[m'.format(p, d, (p / d)))
                else:
                    print('\033[1mR${:.2f} em {}x no cartão com juros, parcelas de R${:.2f}.\033[m'.format(p, d, (p / d * 1.2)))
