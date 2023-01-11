class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        for i in range(int(n/2)):
            temp = s[i]
            s[i] = s[n-i-1]
            s[n-i-1] = temp
        