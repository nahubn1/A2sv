class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        nums = list(count.keys())
        def quickSort(start, end):
            
            if start >= end:
                return

            ptr = start + 1
            for i in range(start+1, end+1):
                
                if count[nums[i]] > count[nums[start]]:
                    
                    nums[i], nums[ptr] = nums[ptr], nums[i]
                    ptr += 1

            nums[start], nums[ptr-1] = nums[ptr-1], nums[start]

            quickSort(start, ptr-2)
            quickSort(ptr, end)

        quickSort(0, len(nums)-1)
        
        return nums[:k]