a = int(input())
b = int(input())
c = int(input())
d = int(input())
for x in range(c,d+1):
  print('\t',x, end='')
for y in range(a,b+1):
  print('\n',y, end='')
  for x in range(c,d+1):
    print('\t', y*x, end='')