class Solution:
    @staticmethod
    def merge(arr1, arr2):
        res = []

        ptr1 = ptr2 = 0
        while ptr1 < len(arr1) and ptr2 < len(arr2):
            if arr1[ptr1][1] < arr2[ptr2][1]:
                res.append(arr1[ptr1])
                ptr1 += 1
            else:
                res.append(arr2[ptr2])
                ptr2 += 1

        return res + arr1[ptr1:] + arr2[ptr2:]
            
    def countSmaller(self, nums: List[int]) -> List[int]:
        count = [0]*len(nums)
        def mergedSort(start, end):
            if start == end:
                return [nums[start]]

            middle = (start+end)//2
            left = mergedSort(start, middle)
            right = mergedSort(middle+1, end)
    
            ptr1 = ptr2 = 0
            while ptr1 < len(left):
                count[left[ptr1][0]] += ptr2
                
                while ptr2 < len(right) and right[ptr2][1] < left[ptr1][1]:
                    count[left[ptr1][0]] += 1
                    ptr2 += 1

                ptr1 += 1

            return self.merge(left, right)

        nums = [(i, val) for i, val in enumerate(nums)]
        mergedSort(0, len(nums)-1)

        return count