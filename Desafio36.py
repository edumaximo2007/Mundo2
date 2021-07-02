import emoji
print('=-='*10)
print('''\033[7m          DESAFIO 36          \033[m''')
print('=-='*10)
print('')
print(emoji.emojize(''':bulb:\033[1mEscreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o\033[m\033[1;31m valor da casa\033[m\033[1m, o \033[1;31msalário\033[m \033[1mdo comprador e em \033[1;31mquantos anos\033[m
\033[1mele vai pagar.

Calcule o valor da prestação mensal, sabendo que ele não pode exceder \033[1;31m30%\033[m \033[1mdo salário ou então o empréstimo será negado.''', use_aliases=True))
print('=-='*40)
print('')
print('''\033[7m        SIMULADOR BANCARIO        \033[m''')
print('')
print('Preencha os dados abaixo para simulação')
casa = float(input('Valor do imovel:R$'))
salario = float(input('Salário do comprador:R$'))
m = int(input('quitação em meses:'))
s = salario * (30/100)
q = casa / m
r = s - q

if r > 0:
    print('\033[1mSeu emprestimo foi aprovado, o valor da sua parcela ficou em R${:.2f}\033[m'.format(q))
else:
    print('Seu emprestimo não foi aprovado, você comprometeu R${:.2f} da sua renda.'.format(r))



