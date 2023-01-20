class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        end = len(arr)-1
        flips = []
        n = len(arr)
        while end > 0:
            max_idx = arr.index(max(arr[:end+1]))
            arr =  arr[max_idx: :-1] + arr[max_idx+1:]
            flips.append(max_idx+1)
            arr = arr[end: :-1] + arr[end+1:]
            flips.append(end+1)
            end -= 1
        
        return flips