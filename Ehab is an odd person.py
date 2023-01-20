n = int(input())
arr = input().split()
odd = int(arr[0])%2
for num in arr:
    if (odd and int(num)%2 != 1) or (not odd and int(num)%2 != 0):
        print(' '.join(sorted(arr, key=lambda x:int(x))))
        break
else:
    print(' '.join(arr))
