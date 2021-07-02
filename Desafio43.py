import emoji
print('=-='*10)
print('''\033[7m          DESAFIO 43          \033[m''')
print('=-='*10)
print('')
print(emoji.emojize(''':bulb: \033[1mDesenvolva uma lógica que leia o peso e altura de uma pessoa, calcule o seu \033[1;32mIMC\033[m\033[1m e mostre seu status,
de acordo com a tabela abaixo:\033[m

\033[1;32m-\033[m\033[1m Abaixo de \033[m\033[1;35m18.5\033[m\033[1m: Abaixo do peso\033[m
\033[1;32m-\033[m\033[1m Entre\033[m\033[1;35m 18.5\033[m\033[1m e\033[m\033[1;35m 25\033[m\033[1m: Peso ideal\033[m
\033[1;32m-\033[m\033[1;35m 25\033[m\033[1m até\033[m\033[1;35m 30\033[m\033[1m: Sobrepeso\033[m
\033[1;32m-\033[m\033[1;35m 30\033[m\033[1m até\033[m\033[1;35m 40\033[m\033[1m: Obsidade\033[m
\033[1;32m-\033[m\033[1m Acima de\033[m\033[1;35m 40\033[m\033[1m: Obesidade mórbida\033[m''', use_aliases=True))
print('')
print('\033[7m Indice de Massa Corporal\033[m')
print('')
print('Preencha o formúlario abaixo.')
n = str(input('\033[1mNome completo: \033[m'))
i = int(input('\033[1mIdade:\033[m'))
p = float(input('\033[1mPeso:\033[m'))
al = int(input('\033[1mAltura em Cm:\033[m'))
m = al**2
a = p / m * 10000
if a <= 18.5:
    print('\033[1m{}, você esta abaixo do peso, seu IMC {:.1f}\033[m'.format(n, a))
elif a <= 25:
    print('\033[1m{}, você está no peso ideal, seu IMC {:.1f}\033[m'.format(n, a))
elif a <= 30:
    print('\033[1m{}, você esta com sobrepeso, seu IMC {:.1f}\033[m'.format(n, a))
elif a <= 40:
    print('\033[1m{}, você esta com obseidade, seu IMC {:.1f}\033[m'.format(n, a))
elif a >= 40:
    print('\033[1m{}, você esta com obesidade mórbida, seu IMC {:.1f}\033[m'.format(n, a))
