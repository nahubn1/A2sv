class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        hashmap[0] = 1

        rSum = 0
        count = 0
        for num in nums:
            rSum += (num%2)
            count += hashmap[rSum-k]
            hashmap[rSum] += 1
        
        return count