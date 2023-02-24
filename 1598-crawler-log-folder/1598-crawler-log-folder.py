class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            opr = log.split('/')[0]
            # print(opr)
            if stack and opr == '..':
                # print('>')
                stack.pop()
            elif opr != '.' and opr != '..':
                # print('>>')
                stack.append(opr)
            # print('______')
        
        # print(stack)
        return len(stack)
        