class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        ans = None
        while start <= end:
            middle = (start+end)//2
            if nums[middle] < target:
                start = middle + 1
            else:
                end = middle - 1

        return start