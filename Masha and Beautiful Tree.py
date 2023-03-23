def invert(arr, s, e):
    ptr1 = s
    ptr2 = ((s+e)//2)+1

    while ptr2 <= e:
        arr[ptr1], arr[ptr2] = arr[ptr2], arr[ptr1]
        ptr1 += 1
        ptr2 += 1
    
def canSort(arr, s, e):
    global count
    if s == e:
        return True

    m = (s+e)//2

    if canSort(arr, s, m) and canSort(arr, m+1, e):
        if arr[m] + 1 == arr[m+1]:
            return True
        elif arr[e] + 1 == arr[s]:
            invert(arr, s, e)
            count += 1
            return True
        else:
            return False
    
    return False


tests = int(input())
for test in range(tests):
    n = int(input())
    perm = list(map(int, input().split()))
    count = 0
    print(count if canSort(perm, 0, n-1) else -1)
