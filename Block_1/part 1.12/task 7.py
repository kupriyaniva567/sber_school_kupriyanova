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