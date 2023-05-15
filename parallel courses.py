from collections import defaultdict, deque
def parallelCourses(n, prerequisites):
    inDegree = [0]*n
    afterTake = defaultdict(list)

    for A, B in prerequisites:
        afterTake[A-1].append(B-1)
        inDegree[B-1] += 1
    
    que = deque()
    visited = set()

    for i in range(n):
        if inDegree[i] == 0:
            que.append(i)

    semester = 1
    taken = 0
    while que:
        for _ in range(len(que)):
            course = que.popleft()
            taken += 1

            if taken == n:
                return semester
            
            for neighbor in afterTake[course]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    que.append(neighbor)
        
        semester += 1
    
    return -1