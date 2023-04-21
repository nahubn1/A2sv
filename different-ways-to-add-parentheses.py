class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        oprs = {'+': lambda a, b: a+b, 
                '-': lambda a, b: a-b,
                '*': lambda a, b: a*b
                }

        stack = [0]
        for char in expression:
            if char.isdigit():
                stack[-1] = stack[-1]*10 + int(char)
            else:
                stack.append(char)
                stack.append(0)
        
        def solve(start, end):
            if start == end:
                return [stack[start]]

            all = []
            for i in range(start, end+1):
                if stack[i] in oprs:
                    opr = oprs[stack[i]]
                    left = solve(start, i-1)
                    right = solve(i+1, end)

                    variations = []
                    for a in left:
                        for b in right:
                            variations.append(opr(a, b))

                    all.extend(variations)

            return all
            
        return solve(0, len(stack)-1)