a=[int(i) for i in input().split()]
a.sort()
m = []
for i in range(len(a)-1):
    if a[i] == a[i+1]:
      if a[i] not in m:
        m.append(a[i])
print(*m)