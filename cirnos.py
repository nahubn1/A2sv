tests = int(input())
for test in range(tests):
    x = int(input())
    y = 1

    if x == 1:
        print(3)
        continue
    
    i = 10
    while i > 0 and not(x & y):
        y <<= 1

    if x == y:
        print(y+1)
    else:
        print(y)
