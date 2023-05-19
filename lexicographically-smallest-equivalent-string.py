class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        rep = {chr(i): chr(i) for i in range(97, 123)}

        def find(char):
            if rep[char] == char:
                return char
            
            rep[char] = find(rep[char])
            return rep[char]

        def union(char1, char2):
            r_char1, r_char2 = find(char1), find(char2)
    
            if r_char1 < r_char2:
                rep[r_char2] = r_char1
            elif r_char1 > r_char2:
                rep[r_char1] = r_char2
    
        for c1, c2 in zip(s1, s2):
            union(c1, c2)
        
        return ''.join([find(c) for c in baseStr])