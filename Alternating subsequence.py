from math import inf
def sign(x):
    return 1 if x > 0 else -1
 
 
tests = int(input())
for test in range(tests):
    n = int(input())
    arr = list(map(int, input().split()))
 
    prev_sign = sign(arr[0])
    max_sum = 0
    maximum = -inf
    for i in range(n):
        
        # when ever sign change is noticed update max sum & reset maximum
        if sign(arr[i]) != prev_sign:
            max_sum += maximum
            maximum = -inf
        
          
        if arr[i] > maximum:
            maximum = arr[i]
        
    
        prev_sign = sign(arr[i])
    
    # sum the maximum of the last subsequence
    max_sum += maximum
    
    print(max_sum)
