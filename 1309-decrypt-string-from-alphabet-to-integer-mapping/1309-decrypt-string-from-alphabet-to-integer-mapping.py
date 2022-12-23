class Solution:
    def freqAlphabets(self, s: str) -> str:
        order = {str(i-96): chr(i) for i in range(97, 123)}
        stack = []
        i = len(s)-1
        # print(order)
        
        while i >= 0:
            if s[i] == '#':
                
                stack.append(order[s[i-2:i]])
                i -= 3
            else:
                
                stack.append(order[s[i]])
                i -= 1
                
        # print(stack)
        return ''.join(reversed(stack))  