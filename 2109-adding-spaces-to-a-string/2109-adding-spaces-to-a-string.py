class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        start = 0
        for end in spaces:
            res.append(s[start:end])
            start = end
        res.append(s[start:])            
        return ' '.join(res)