class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        hashmap = defaultdict(int)
        for num in arr:
            hashmap[num] = hashmap[num - difference] + 1
        
        return max(hashmap.values())