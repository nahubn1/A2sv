class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        slopes = []
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                slope = 1
            elif arr[i] == arr[i-1]:
                slope = 0
            else:
                slope = -1
                
            if not(slopes and slopes[-1] == slope):
                slopes.append(slope)
                
        return slopes == [1, -1]
                
                
                