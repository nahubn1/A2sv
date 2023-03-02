class Solution:
    def swap(self, start, end):
        if start >= end:
            return

        self.s[start], self.s[end] = self.s[end], self.s[start] 
        self.swap(start+1, end-1)
        
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.s = s
        self.swap(0, len(s)-1)
