class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.ans = []

        def backtrack(start, arr):
            if len(arr) > 4:
                return

            if start == len(s):
                if len(arr) == 4:
                    self.ans.append('.'.join(arr))

            for i in range(start, len(s)):
                if 0 <= int(s[start:i+1]) <= 255 and ((len(s[start:i+1])) == 1 or s[start] != "0"):
                    backtrack(i+1, arr+[s[start:i+1]])
        
        backtrack(0, [])
        return self.ans