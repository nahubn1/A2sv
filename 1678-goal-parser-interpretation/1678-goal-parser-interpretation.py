class Solution:
    def interpret(self, command: str) -> str:
        stack = []
        for char in command:
            if char == ')':
                if stack[-1] == '(':
                    stack.pop()
                    stack.append('o')
            elif char == 'a':
                stack.pop()    
                stack.append(char)
            else:
                stack.append(char)
        
        return ''.join(stack)