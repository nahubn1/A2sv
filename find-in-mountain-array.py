# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()  

        left, right = 0, n-2
        while left <= right:
            middle = (left+right)//2

            if mountain_arr.get(middle) < mountain_arr.get(middle+1):
                left = middle + 1
            else:
                right  = middle - 1
            
        
        start, end = 0, left
        while start <= end:
            middle = (start+end)//2
            val = mountain_arr.get(middle)

            if val == target:
                return middle
            elif val < target:
                start  = middle + 1
            else:
                end = middle - 1
        
        start, end = left, n-1
        while start <= end:
            middle = (start+end)//2
            val = mountain_arr.get(middle)

            if val == target:
                return middle
            elif val > target:
                start  = middle + 1
            else:
                end = middle - 1
        
        return -1