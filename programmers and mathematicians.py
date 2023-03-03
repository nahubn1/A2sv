def isvalid(p, m, t):
    minn = min(p, m)
    maxx = max(p, m)
    a2 = (maxx-minn)/2
    a1 = (minn-a2)/2
    intersection = [a1, a2] if a1>= 0 and a2>=0 else [0, 0]
    return t <= max([int(minn/2), int(min(minn, maxx/3)), int(sum(intersection))])

tests = int(input())
for test in range(tests):
    a, b = map(int, input().split())
    start, end = 1, ((a+b)//4)+1
    while start <= end:
        middle = (start+end)//2
        if not isvalid(a, b, middle):
            end = middle - 1
        elif isvalid(a, b, middle) and isvalid(a, b, middle+1):
            start = middle + 1
        else:
            print(middle)
            break
    else:
        print(0)
