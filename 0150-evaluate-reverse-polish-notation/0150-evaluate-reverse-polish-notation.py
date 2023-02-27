class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        oprs = {'+', '-', '*','/'}
        stack = []
        for token in tokens:
            if token in oprs:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(eval(f'{num1}{token}{num2}')))
            else:
                stack.append(token)
        
        return int(stack[0])

        