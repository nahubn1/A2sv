class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        hashmap = defaultdict(int)
        hashmap[0] = 1
        
        count = 0
        rSum = 0
        
        for num in nums:
            rSum += num
            count += hashmap[rSum%k]
            hashmap[rSum%k] += 1
        
        return count
        
        