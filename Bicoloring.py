from collections import defaultdict
n = int(input())

while n != 0:
    edges = int(input())

    graph = defaultdict(list)
    for edge in range(edges):
        u, v = map(int, input().split())

        graph[u].append(v)
        graph[v].append(u)

    color = defaultdict(int)
    def dfs(root):
        
        stack = [(root, 1)]

        while stack:
            node, col = stack.pop()
            if color[node] == 0:
                color[node] = col
                for neigbor in graph[node]:
                    stack.append((neigbor, -col))
            elif color[node] == -col:
                return False
        
        return True
    
    for i in range(1, n):
        if color[i] == 0 and not dfs(i):
            print('NOT BICOLOURABLE.')
            break
    else:
        print('BICOLOURABLE.')
    
    n = int(input())
    
    


