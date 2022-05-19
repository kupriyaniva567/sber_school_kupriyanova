a=int(input())
b=int(input())
c=int(input())
p=((a+b+c)/2)
S=(p*((p-a)*(p-b)*(p-c)))
print(S**0.5)

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

num = int(input())
b = float('inf') #для обозначения бесконечной
if -15<num<=12 or 14<num<17 or 19<=num<b: # (−15,12]∪(14,17)∪[19,+∞)
    print('True')
else:
    print('False')

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
