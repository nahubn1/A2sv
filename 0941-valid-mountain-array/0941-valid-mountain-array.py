class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        slope = None
        for i in range(len(arr)-1):
            if slope is None:
                if arr[i+1] > arr[i]:
                    slope = 'UP'
                else:
                    return False
            
            if slope == 'UP':
                if arr[i+1] < arr[i]:
                    slope = 'DOWN'
                elif arr[i+1] == arr[i]:
                    return False
                
            if slope == 'DOWN' and arr[i+1] >= arr[i]:
                return False
            
        return slope == "DOWN"
                
                       
                
                
                