class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        result = []
        for i, num in enumerate(nums):
            if num == target:
                result.append(i)
        return result

        
        