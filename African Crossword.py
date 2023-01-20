from collections import Counter
m, n = map(int, input().split())
grid = []
for i in range(m):
    grid.append(list(input()))
 
removed = set()
# row scan
for i in range(m):
    count = Counter(grid[i])
    for j in range(n):
        if count[grid[i][j]] > 1:
            removed.add((i, j))
 
# column scan
for j in range(n):
    column = []
    for i in range(m):
        column.append(grid[i][j])
 
    count = Counter(column)
    for i in range(m):
        if count[grid[i][j]] > 1:
            removed.add((i, j))
 
for i in range(m):
    for j in range(n):
        if (i, j) not in removed:
            print(grid[i][j], end='')
