class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        a = [0, len(strs[0])] 
        for i, x in enumerate(strs):
            if len(x) < a[1]:
                a = [i, len(x)]
        
        j = 0
        otp = ""
        while j < a[1]:
            comp = strs[a[0]][j]
            for word in strs:
                if comp != word[j]:
                    return otp
            otp += comp
            j += 1
        
        return otp