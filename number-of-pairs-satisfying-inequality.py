class Solution:
    @staticmethod
    def merge(arr1, arr2):
        res = []
        ptr1 = ptr2 = 0
        while ptr1 < len(arr1) and ptr2 < len(arr2):
            if arr1[ptr1] < arr2[ptr2]:
                res.append(arr1[ptr1])
                ptr1 += 1
            else:    
                res.append(arr2[ptr2])
                ptr2 += 1

        return res + arr1[ptr1:] + arr2[ptr2:]

    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        self.count = 0
        self.diff = diff
        nums = [nums1[i]-nums2[i] for i in range(len(nums1))]
        def mergedSort(start, end):
            if start == end:
                return [nums[start]]

            middle = (start+end)//2

            left = mergedSort(start, middle)
            right = mergedSort(middle+1, end)

            lcount = 0
            ptr1 = len(left)-1
            ptr2 = len(right)-1
            while ptr1 >= 0:
                self.count += (len(right) - (ptr2+1))
                while ptr2 >= 0 and left[ptr1] - self.diff <= right[ptr2]:
                    self.count += 1
                    ptr2 -= 1

                ptr1 -= 1

            return self.merge(left, right)

        mergedSort(0, len(nums)-1)
        
        return self.count