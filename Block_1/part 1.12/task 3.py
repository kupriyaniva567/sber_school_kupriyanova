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