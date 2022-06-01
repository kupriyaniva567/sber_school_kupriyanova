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
if (a <= b and a >= c) or (a >=b and a <= c):
    print (a)
elif (b <= c and b >=a) or (b >= c and b <= a):
    print (b)
else:
    print (c)