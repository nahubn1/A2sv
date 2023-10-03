class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:            
            if stack and stack[-1][0] == char:
                if stack[-1][1] == k-1:
                    stack.pop() 
                else:
                    stack[-1][1] += 1
            else:
                stack.append([char, 1])

        ans = []
        for char, freq in stack:
            ans.extend([char]*freq)

        return ''.join(ans)