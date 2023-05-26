class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)

        for i in range(n-1, -1, -1):
            k = -1
            for j in range(i, n):
                if arr[j] < arr[i]:
                    if k == -1 or arr[j] > arr[k]:
                        k = j
            
            if k != -1:
                arr[i], arr[k] = arr[k], arr[i]
                break
   
        return arr