n = int(input( ))
count = 0
for i in range(1, n):
    for a in range(i):
        if count == n:
            break
        count += 1
        print(i, end=' ')