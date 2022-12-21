class Solution:
    def isPalindrome(self, x: int) -> bool:
        if ''.join(reversed(list(str(x)))) == str(x):
            return True
        else:
            return False
        
        