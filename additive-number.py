class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def backtrack(start, arr):
            if start == len(num):
                return len(arr) >= 3
             
            for i in range(start, len(num)):
                if num[start] != "0" or i==start:
                    if len(arr) < 2 or arr[-1]+arr[-2] == int(num[start:i+1]):
                        if backtrack(i+1, arr + [int(num[start:i+1])]):
                            return True
            
        return backtrack(0, [])