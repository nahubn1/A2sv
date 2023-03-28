class Solution:
    @staticmethod
    def merge(arr1, arr2):
        ptr1, ptr2  = 0, 0
        res = []
        while ptr1 < len(arr1) and ptr2 < len(arr2):
            if arr1[ptr1] < arr2[ptr2]:
                res.append(arr1[ptr1])
                ptr1 += 1
            else:
                res.append(arr2[ptr2])
                ptr2 += 1
        
        return res + arr1[ptr1:] + arr2[ptr2:]

    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0

        def mergeSort(start, end):
            if start == end:
                return [nums[start]]
            
            middle = (start+end)//2
            left = mergeSort(start, middle)
            right = mergeSort(middle+1, end)

            for num in left:
                self.count += bisect_left(right, num/2) 
            
            return self.merge(left, right)
        
        mergeSort(0, len(nums)-1)

        return self.count
