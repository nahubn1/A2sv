class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        hashmap = defaultdict(list)
        for num in nums:
            if num-1 in hashmap:
                seq_len = heappop(hashmap[num-1])
                heappush(hashmap[num], seq_len+1)

                if not hashmap[num-1]:
                    del hashmap[num-1]
            else:
                heappush(hashmap[num], 1)
        
        for num in hashmap:
            if any(i < 3 for i in hashmap[num]):
                return False
        
        return True