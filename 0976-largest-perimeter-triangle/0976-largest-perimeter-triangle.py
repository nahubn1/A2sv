class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # area of a triangle with sides a, b & c = sqrt(s(s-a)(s-b)(s-c)).
        # where s = (a+b+c).
        # thus all the sides should be greater than s to have a postive area.
        
        nums.sort()
        for i in range(len(nums)-1, 1, -1):
            s = (nums[i]+nums[i-1]+nums[i-2])/2
            if nums[i] < s:
                return nums[i]+nums[i-1]+nums[i-2]
        else:
            return 0