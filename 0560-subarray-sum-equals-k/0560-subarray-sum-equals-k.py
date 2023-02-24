class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        rSum = 0
        hashmap = defaultdict(int)
        hashmap[0] = 1
        count = 0
        
        for num in nums:
            rSum += num
            count += hashmap[rSum-k]
            hashmap[rSum] += 1
        
        return count
        