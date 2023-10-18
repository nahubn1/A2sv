class Solution:
    def calculate(self, s: str) -> int:
        order = [{ '/': lambda n1, n2: n1 // n2, '*': lambda n1, n2: n1 * n2}, 
                {'-': lambda n1, n2: n1 - n2, '+': lambda n1, n2: n1 + n2}]

        exp = []
        for char in s:
            if char.isspace():
                continue

            if exp and char.isdigit() and type(exp[-1]) is int:
                exp[-1] *= 10
                exp[-1] += int(char)
            else:
                exp.append(int(char) if char.isdigit() else char)
        
        for i in range(2):
            stack = []

            for item in exp:
                if stack and stack[-1] in order[i]:
                    opr = stack.pop()
                    n1 = stack.pop()
                    n2 = item
                    stack.append(order[i][opr](n1, n2))
                else:
                    stack.append(item)

            exp = stack[:]
            
    
        return exp[0]