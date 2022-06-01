num = int(input()) #Количество программистов
if num % 10 == 1 and num%100 != 11:
    print(num, 'программист')
elif num%10 in [2, 3, 4] and not num%100 in [12, 13, 14]:
    print(num, 'программиста')
else:
    print(num, 'программистов')