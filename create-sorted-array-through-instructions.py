from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        nums = SortedList()
        total_cost = 0

        for i in instructions:
            total_cost += min(nums.bisect_left(i), len(nums) - nums.bisect_right(i))
            nums.add(i)
            
        return total_cost % (10**9+7)