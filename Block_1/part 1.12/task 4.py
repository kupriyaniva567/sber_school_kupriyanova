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