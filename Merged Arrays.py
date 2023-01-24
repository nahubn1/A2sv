m, n = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
 
ptr1, ptr2 = 0, 0
merged = []
for i in range(m+n):
    if ptr1 < m and ptr2 < n:
        if arr1[ptr1] < arr2[ptr2]:
            merged.append(str(arr1[ptr1]))
            ptr1 += 1
        else:
            merged.append(str(arr2[ptr2]))
            ptr2 += 1
    else:
        if ptr1 < m:
            merged.append(str(arr1[ptr1]))
            ptr1 += 1
        elif ptr2 < n:
            merged.append(str(arr2[ptr2]))
            ptr2 += 1
            
print(' '.join(merged))
