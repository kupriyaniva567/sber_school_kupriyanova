digit = 0
while digit <= 100:
  digit = int (input())
  if digit > 100:
    break
  if digit < 10:
    continue
  print(digit)