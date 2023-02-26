class Solution:
    def canChange(self, start: str, target: str) -> bool:
        
        start = list(start)
        target = list(target)

        lastMatch = -1
        for i in range(len(target)):
            if target[i] == 'L':
                for j in range(max(i, lastMatch+1), len(start)):
                    if start[j] == 'L':
                        start[i], start[j] = start[j], start[i]
                        lastMatch = j
                        break
                    elif start[j] == 'R':
                        return False
                else:
                    return False

        lastMatch = len(start)
        for i in range(len(target)-1, -1, -1):
            if target[i] == 'R':
                for j in range(min(i, lastMatch+1), -1, -1):
                    if start[j] == 'R': 
                        start[i], start[j] = start[j], start[i]
                        lastMatch = j
                        break

                    elif start[j] == 'L':
                        return False
                else:
                    return False

        return start == target