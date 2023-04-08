class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        x, y = edges[0]
        return x if x in edges[1] else y