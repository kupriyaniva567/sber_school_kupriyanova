    year = int(input())
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('Високосный')
    elif year % 4 != 0 and year % 400 != 0 or year % 100 == 0:
        print('Обычный')