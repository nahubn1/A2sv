#User function Template for python3

class Solution: 
    def select(self, arr, i):
        minn = i
        for j in range(i, len(arr)):
            if arr[j] < arr[minn]:
                minn = j
        return minn
    
    def selectionSort(self, arr,n):
        for i in range(n):
            minn = self.select(arr, i)
            arr[i], arr[minn] = arr[minn], arr[i]
            
