class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        output = []
        lock = False
        last_char = None
        for line in source:
            if not lock:
                stack = []
            for char in line:
                # print(last_char,char, end = '->')
                if not lock and stack and last_char == '/' and char == '*':
                    stack.pop()
                    lock = True
                    last_char = None
                elif lock and last_char == '*' and char == '/':
                    lock = False
                    last_char = None
                    continue
                else:
                    last_char = char
                # print(lock)
                if not lock:
                    if stack and stack[-1] == char == '/':
                        stack.pop()
                        break
                    else:
                        stack.append(char)
            
            if not lock:
                output.append(''.join(stack))
            
        return [i for i in output if i!=""]