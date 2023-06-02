class Solution:
    def bulbSwitch(self, n: int) -> int:
        
        ans = 0
        while (ans+1)**2 <= n:
            ans += 1
            
        return ans