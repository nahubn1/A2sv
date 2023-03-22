class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.maxLen = 0

        def backtrack(start, s):
            self.maxLen = max(self.maxLen, len(s))

            for i in range(start, len(arr)):
                if len(arr[i]) == len(set(arr[i])) and all([char not in s for char in arr[i]]):
                    backtrack(i+1, s+arr[i])
        
        backtrack(0, '')

        return self.maxLen