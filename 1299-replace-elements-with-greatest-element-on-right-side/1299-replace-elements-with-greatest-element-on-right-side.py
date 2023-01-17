class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n-1, -1, -1):
            if i == n-1:
                last = arr[i]
                arr[i] = -1
            else:
                temp = arr[i]
                arr[i] = max(last, arr[i+1])
                last = temp
        
        return arr