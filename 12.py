a = int(input())
b = int(input())
if b !=0:
    print(a/b)
else:
    print('деление невозможно')
    b = int(input('Введите ненулевое значение '))
    if b == 0:
        print('Вы не справились')
    else:
        print(a/b)


