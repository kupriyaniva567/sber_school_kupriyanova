A = int(input()) #рекомендуемое время сна для человека
B = int(input()) #не рекомендуется спать более этого времени
H = int(input()) #время сна сейчас
if A <= H and H <= B:
    print('Это нормально')
elif H >= B :
    print('Пересып')
elif H < A:
    print('Недосып')

    year = int(input())
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('Високосный')
    elif year % 4 != 0 and year % 400 != 0 or year % 100 == 0:
        print('Обычный')