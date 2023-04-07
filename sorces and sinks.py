from collections import defaultdict
n = int(input())

out = set()
into = set()
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j]:
            out.add(i+1)
            into.add(j+1)

print(n-len(into), *sorted(set(range(1, n+1)) - set(into)))
print(n-len(out), *sorted(set(range(1, n+1)) - set(out)))