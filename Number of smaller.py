m, n = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

ptr = 0
result = []
for i in range(n):
    while ptr < m and arr1[ptr] < arr2[i]:
        ptr += 1
    
    result.append(str(ptr))
    
print(' '.join(result))
