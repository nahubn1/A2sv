from typing import List
from collections import defaultdict, deque

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        afterComes = defaultdict(list)
        preReq = [0]*n
        for U, V in edges:
            afterComes[U-1].append(V-1)
            preReq[V-1] += 1
        
        que = deque()
        finished = set()
        
        for i in range(n):
            if preReq[i] == 0:
                que.append(i)
                finished.add(i)
        
        timeTaken = [0]*n
        time = 1
        while que:
            
            for _ in range(len(que)):
                job = que.popleft()
                timeTaken[job] = str(time)
                for after in afterComes[job]:
                    preReq[after] -= 1
                    if preReq[after] == 0:
                        que.append(after)
            
            time += 1
        
        return ' '.join(timeTaken)