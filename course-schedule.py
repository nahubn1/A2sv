class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0]*numCourses
        takeAfter = defaultdict(set)
        for a, b in prerequisites:
            inDegree[b] += 1
            takeAfter[a].add(b)
        
        que = deque()
        for course in range(numCourses):
            if not inDegree[course]:
                que.append(course)
        
        schedule = []
        
        while que:
            
            course = que.popleft()
            schedule.append(course)

            for dependet in takeAfter[course]:
                inDegree[dependet] -= 1
                if not inDegree[dependet]:
                    que.append(dependet)
        
        
        return len(schedule) == numCourses