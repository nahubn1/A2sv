class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        start, end = 0, n-1
        while start <= end:
            middle = (start+end)//2
            if n-middle > citations[middle]:
                start = middle + 1
            else:
                end = middle - 1
        
        return n-start