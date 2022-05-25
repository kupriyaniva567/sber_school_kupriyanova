#Задача 1
a=int(input())
b=int(input())
c=int(input())
p=((a+b+c)/2)
S=(p*((p-a)*(p-b)*(p-c)))
print(S**0.5)
#Задача 2
num = int(input())
b = float('inf') #для обозначения бесконечной
if -15<num<=12 or 14<num<17 or 19<=num<b: # (−15,12]∪(14,17)∪[19,+∞)
    print('True')
else:
    print('False')
#Задача 3
num1 = float(input()) #Первое число
num2 = float(input()) #Второе число
operation = str(input()) #Операция
if operation == '+':
   print(num1+num2)
elif operation == '-':
    print(num1-num2)
elif operation == '/' and num2 == 0:
    print('Деление на 0!')
elif operation == '/' and num2 != 0:
    print(num1/num2)
elif operation == '*':
    print(num1 * num2)
elif operation == 'mod' and num2 == 0:
    print('Деление на 0!')
elif operation == 'mod' and num2 != 0:
    print(num1%num2)
elif operation == 'pow' and num1 != 0:
    print(num1**num2)
elif operation == 'div' and num2 == 0:
    print('Деление на 0!')
elif operation == 'div' and num2 != 0:
    print(num1//num2)
#Задача 4
shape = str(input())
if shape == 'треугольник':
    a = int(input()) #сторона треугольника
    b = int(input()) #сторона треугольника
    c = int(input()) #сторона треугольника
    i=((a+b+c)/2)
    print((i*((i-a)*(i-b)*(i-c)))**0.5)
elif shape == 'прямоугольник':
    a = int(input()) #сторона прямоугольника
    b = int(input()) #сторона прямоугольника
    print(a*b)
elif shape == 'круг':
    r = float(input()) #радиус
    pi = 3.14
    print (pi*(r**2))
#Задача 5
a = int(input())
b = int(input())
c = int(input())
# поиск max значения
if a >= b and a >= c:
    print(a)
elif b >= c and b >= a:
    print(b)
elif a <= c >= b:
    print(c)
# поиск min значения
if a <= b and a <= c:
    print(a)
elif b <= a and b <= c:
    print(b)
elif a >= c <= b:
    print(c)
# оставшееся значение
#Задача 6
num = int(input()) #Количество программистов
if num % 10 == 1 and num%100 != 11:
    print(num, 'программист')
elif num%10 in [2, 3, 4] and not num%100 in [12, 13, 14]:
    print(num, 'программиста')
else:
    print(num, 'программистов')
#Задача 7
number = input() #номер билета состоит из 6 цифр
# print(number[0])
# print(number[1])
# print(number[2])
# print(number[3])
# print(number[4])
# print(number[5])
if (int(number[0])+int(number[1])+int(number[2])) == (int(number[3])+int(number[4])+int(number[5])):
    print('Счастливый')
else:
    print('Обычный')