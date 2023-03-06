class Solution:
    def isvalid(self, d):
        total = 0
        for num in self.nums:
            total += ceil(num/d)

        return total <= self.threshold

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        self.nums = nums
        self.threshold = threshold
        start, end = 1, max(nums)
        while start <= end:
            middle = (start+end)//2
            if not self.isvalid(middle):
                start = middle + 1
            else:
                end = middle - 1
        
        return start