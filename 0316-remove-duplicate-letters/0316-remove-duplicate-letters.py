class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        count = Counter(s)
        
        for char in s:
            count[char] -= 1
            if char not in stack:
                while stack and ord(stack[-1]) >= ord(char) and count[stack[-1]] >= 1:
                    stack.pop()
                else:
                    stack.append(char) 

                
        return ''.join(stack)