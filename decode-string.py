class Solution:
    def decodeString(self, s: str) -> str:
        if s.isdigit():
            return ''
            
        stack = []
        for i in range(len(s)):
            if s[i] == ']':
                content = []
                while stack[-1] != '[':
                    content.append(stack.pop())
                else:
                    content.reverse()
                    stack.pop()

                k, j = 0, 1
                while stack and stack[-1].isdigit():
                    k += j*int(stack.pop())
                    j *= 10

                stack.extend([*k*content])

            else:
                stack.append(s[i])
            
        return ''.join(stack)