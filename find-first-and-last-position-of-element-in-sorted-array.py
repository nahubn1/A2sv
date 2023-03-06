class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = 0, len(nums)-1
        left = -1
        while start <= end:
            middle = (start+end)//2
            if nums[middle] < target:
                start = middle + 1
            elif nums[middle] > target:
                end = middle - 1
            elif middle != 0 and nums[middle] == target and nums[middle-1] == target:
                end = middle - 1
            else:
                left = middle
                break
        else:
            return [-1, -1]
        
        start, end = 0, len(nums)-1
        right = -1
        while start <= end:
            middle = (start+end)//2
            if nums[middle] > target:
                end = middle - 1
            elif nums[middle] < target:
                start = middle + 1
            elif middle != len(nums)-1 and nums[middle] == target and nums[middle+1] == target:
                start = middle + 1
            else:
                right = middle
                break
        else:
            return [-1, -1]

        
        return [left, right]