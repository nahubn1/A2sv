class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        
        empire = {i: [i, n-1] for i in range(n)}
        mon_stack = []
        
        for i in range(n):
            while mon_stack and arr[mon_stack[-1]] > arr[i]:
                defeated = mon_stack.pop()
                
                empire[i][0] = empire[defeated][0]
                empire[defeated][1] = i-1
            
            mon_stack.append(i)
            
        tot = 0
        for i in empire:
            start = empire[i][0]
            end = empire[i][1]
            
            tot += arr[i]*(i-start+1)*(end-i+1)
        
        return tot % (10**9+7)
            