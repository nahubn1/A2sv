class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0
        def sort(start, arr):
            if start == len(nums)-1:
                return 

            num = arr[start]
            sort(start+1, nums)

            self.count += (bisect_left(arr, num/2, lo=start+1) - start - 1)

            i = bisect_right(arr, num, lo=start)
            arr.insert(i, num)
            arr.pop(start)
                
                
        
        sort(0, nums)

        return self.count