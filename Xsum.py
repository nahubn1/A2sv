tests = int(input())
for test in range(tests):
    n, m = map(int, input().split())
    diag = {i: 0 for i in range(n+m-1)}
    anti_diag = {i: 0 for i in range(-m+1, n)}
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
        for j in range(m):
            diag[i+j] += row[j]
            anti_diag[i-j] += row[j]
            
    max_pos = 0
    for i in range(n):
        for j in range(m):
            max_pos = max(diag[i+j]+anti_diag[i-j]-matrix[i][j], max_pos)
            
    print(max_pos)
