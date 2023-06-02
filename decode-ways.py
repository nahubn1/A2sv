class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dp(string):
            
            if string in memo:
                return memo[string]

            if string[0] == '0':
                return 0

            if len(string) == 1:
                return 1
            elif len(string) == 2:
                ans = 0
                
                if int(string) <= 26:
                    ans += 1
                if string[-1] != '0':
                    ans += 1 

                return ans


            path2 = 0
            if int(string[:2]) <= 26:
                path2 += dp(string[2:])
            memo[string] = dp(string[1:]) + path2
            return memo[string]

        return dp(s)