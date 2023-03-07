class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ends  = [interval[1] for interval in intervals]
        starts = [interval[0] for interval in intervals]
        starts_idx = list(range(len(starts)))
        starts_idx.sort(key=lambda x:starts[x])
        
        
        ans = []
        for end in ends:
            left, right = 0, len(intervals)-1 
            while left <= right:
                middle  = (left+right)//2
                if end > starts[starts_idx[middle]]:
                    left = middle + 1
                else:
                    right = middle - 1
            
            ans.append(starts_idx[left] if left < len(intervals) else -1)
        
        return ans