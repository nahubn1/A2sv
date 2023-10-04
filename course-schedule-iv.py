class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        pre_req = [[False]*numCourses for _ in range(numCourses)]

        for u, v in prerequisites:
            pre_req[u][v] = True
        
        for k in range(numCourses):
            for i in  range(numCourses):
                for j in range(numCourses):
                    pre_req[i][j] = pre_req[i][j] or (pre_req[i][k] and pre_req[k][j])
        
        return [pre_req[u][v] for u, v in queries]