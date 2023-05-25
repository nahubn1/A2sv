class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        flag = [0]*n
        minSoFar = inf
        for i in range(n):
            if nums[i] > minSoFar:
                flag[i] = 1
            else:
                minSoFar = nums[i]
        
        maxSoFar = -inf
        for i in range(n-1, -1, -1):
            if nums[i] < maxSoFar:
                if flag[i]: return True
            else:
                maxSoFar = nums[i]

        return False