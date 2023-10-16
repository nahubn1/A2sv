class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        minn = min(nums)
        maxx = max(nums)

        return max(maxx-minn-2*k, 0)