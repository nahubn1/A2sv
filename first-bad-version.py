# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n

        while start <= end:
            middle = (start+end)//2
            if not isBadVersion(middle):
                start = middle + 1
            elif isBadVersion(middle) and isBadVersion(middle-1):
                end = middle - 1 
            else:
                return middle