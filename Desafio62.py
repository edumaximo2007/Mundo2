print('=-='*10)
print('''\033[7m          DESAFIO 62          \033[m''')
print('=-='*10)
import emoji
print(emoji.emojize(''':bulb: \033[1mMelhore o\033[m\033[1;32m DESAFIO 061\033[m\033[1m, pergutando para o usuário se ele quer
mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar\033[m\033[1;35m O termos\033[m\033[1m.\033[m''',use_aliases=True))
print('')
print('\033[7m PROGRESSÃO ARITIMETICA V3.0\033[m')
print('')
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(emoji.emojize('{} :arrow_right:'.format(termo), use_aliases=True), end='')
        termo += razão
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão aritietica finalizada com {} termos mostrados'.format(total))