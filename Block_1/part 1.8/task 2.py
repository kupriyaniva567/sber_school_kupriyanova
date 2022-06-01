X = int(input()) #всего минут
H = int(input()) #часы
M = int(input()) #минуты
c = (H*60 + M) + X
print(c//60)
print(c%60)