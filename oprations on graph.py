from collections import defaultdict
n = int(input())
k = int(input())

graph = defaultdict(list)
for i in range(k):
    opr = input().split()
    if opr[0] == '1':
        u, v = opr[1:]
        graph[u].append(v)
        graph[v].append(u)
    else:
        v = opr[-1]
        print(*graph[v])