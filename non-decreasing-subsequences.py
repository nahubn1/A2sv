class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        def backtrack(start, arr):
            if len(arr) >= 2 and tuple(arr) not in ans:
                ans.add(tuple(arr))

            for i in range(start, len(nums)):
                if not arr or arr[-1] <= nums[i]:
                    backtrack(i+1, arr+[nums[i]])
            
        backtrack(0, [])
        return ans