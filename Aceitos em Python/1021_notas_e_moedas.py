valor = float(input())

print('NOTAS:')
notas = [10000, 5000, 2000, 1000, 500, 200]
moedas = [100, 50, 25, 10, 5, 1]
valor *=100
for nota in notas:
    print('{} nota(s) de R$ {:.2f}'.format(int(valor/nota),nota/100))
    valor%=nota

print('MOEDAS:')
for moeda in moedas:
    print('{} moeda(s) de R$ {:.2f}'.format(int(valor/moeda),moeda/100))
    valor%=moeda

