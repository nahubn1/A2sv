class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            opr = log.split('/')[0]
            if stack and opr == '..':
                stack.pop()
            elif opr != '.' and opr != '..':
                stack.append(opr)
        
        return len(stack)
        