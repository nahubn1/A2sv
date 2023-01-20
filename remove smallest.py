tests = int(input())
for test in range(tests):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    elem = arr[0]
    for num in arr:
        if num-elem <= 1:
            elem = num
        else:
            print('NO')
            break
    else:
        print('YES')
