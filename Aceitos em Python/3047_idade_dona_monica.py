idade_monica = int(input())

idade_A = int(input())

idade_B = int(input())

if(idade_monica >= 40 and idade_monica <=110):
    if (idade_A >= 1 and idade_A <= idade_monica):
        if (idade_B >= 1 and idade_B <= idade_monica and idade_B != idade_A):
            idade_C = idade_monica - idade_A - idade_B
            print(max([idade_A,idade_B,idade_C],key=int))
            