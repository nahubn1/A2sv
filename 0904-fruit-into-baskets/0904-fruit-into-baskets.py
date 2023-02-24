class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = Counter([])
        start = 0
        maxFru = 0
        for end in range(len(fruits)):
            count[fruits[end]] += 1
            
            while len(count) > 2:
                count[fruits[start]] -= 1
                if count[fruits[start]] == 0: del count[fruits[start]]
                start += 1
                
            maxFru = max(maxFru, end-start+1)
        
        return maxFru
        