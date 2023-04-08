n = int(input())
for i in range(n):
    row = list(map(int, input().split()))
    into = []
    for j in range(n):
        if row[j] == 1:
            into.append(j+1)
        
    print(len(into), *into)