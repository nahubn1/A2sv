class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        rSum = 0
        hashmap = defaultdict(int)
        hashmap[0] = 1
        count = 0
        for num in nums:
            rSum += num
            count += hashmap[rSum-goal]
            hashmap[rSum] += 1

        return count