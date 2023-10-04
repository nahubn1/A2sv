class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        def belowCount(num):
            if num == 0:
                return n+1
            
            mul = 10
            ans = 0
            while num*mul <= n:
                l = num*mul
                r = min(((num+1)*mul)-1, n)

                ans += r - l + 1
                mul *= 10
        
            return ans

        def dfs(num, i):           
            if i == k:
                return num
            
            bel_cnt = belowCount(num)

            if k <= i + bel_cnt:
                return dfs(num*10, i+1)
            else:
                if num+1 <= n:
                    return dfs(num+1, i+bel_cnt+1)
                else:
                    return dfs(num//10 + 1, i+bel_cnt+1)
        
        return dfs(1, 1)