num = float(input())

if (num >=0 and num <= 100):
    if num <= 50:
        if num > 25:
            print('Intervalo (25,50]')
        else:
            print('Intervalo [0,25]')
    else:
        if (num <= 75):
            print('Intervalo (50,75]')
        else:
            print('Intervalo (75,100]')
else:
    print('Fora de intervalo')