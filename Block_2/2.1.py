a=5
while a>0:
    print(a, end=' ')
    a -= 1

i = 0
while i <= 10:
    i = i + 1
    if i > 7:
        i = i + 2
        print(i)

i = 0
while i <= 10:
    i = i + 1
    if i > 7:
        i = i + 2
        print(i)

i = 0
while i < 5:
    print('*')
    if i % 2 == 0:
        print('**')
    if i > 2:
        print('***')
    i = i + 1

a = None
summa = 0
while a !=0:
    a=int(input())
    summa += a
print(summa)