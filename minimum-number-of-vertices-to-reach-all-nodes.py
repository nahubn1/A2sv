class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        notSource = set()
        for form_, to_ in edges:
            notSource.add(to_)

        return set(range(0, n)) - notSource