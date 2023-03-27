class Solution:
    def quickSort(self, arr, start, end):
        if start >= end:
            return
        
        pivot = start
        ptr = start+1
        for i in range(start+1, end+1):
            if arr[i] < arr[pivot]:
                arr[i], arr[ptr] = arr[ptr], arr[i]
                ptr += 1
    
        arr[pivot], arr[ptr-1] = arr[ptr-1], arr[pivot]
        
        self.quickSort(arr, start, ptr-2)
        self.quickSort(arr, ptr, end)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        shuffle(nums)
        self.quickSort(nums, 0, len(nums)-1)
        return nums[-k]