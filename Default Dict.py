# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n, m = map(int, input().split(' '))
A = [input() for i in range(n)]
B = [input() for i in range(m)]
posA = defaultdict(lambda: ['-1'])
for i in range(n):
    if A[i] in posA:
        posA[A[i]].append(str(i+1))
    else:
        posA[A[i]] = [str(i+1)]
for char in B:
    print(' '.join(posA[char]))
