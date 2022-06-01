num = int(input())
b = float('inf') #для обозначения бесконечной
if -15<num<=12 or 14<num<17 or 19<=num<b: # (−15,12]∪(14,17)∪[19,+∞)
    print('True')
else:
    print('False')