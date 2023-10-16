class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1: return 0

        n1 = ceil(len(nums)/2)
        n2 = floor(len(nums)/2)

        count1 = defaultdict(int)
        count2 = defaultdict(int)

        for i in range(len(nums)):
            if i % 2 == 0:
                count1[nums[i]] += 1
            else:
                count2[nums[i]] += 1
        
        choice1 = sorted(count1, key = count1.get, reverse=True)
        choice2 = sorted(count2, key = count2.get, reverse=True)
        
        if choice1[0] != choice2[0]:
            return n1-count1[choice1[0]] + n2-count2[choice2[0]]
        else:
            if len(choice1) > 1 and len(choice2) > 1:
                return min(n1-count1[choice1[0]] + n2-count2[choice2[1]], n1-count1[choice1[1]] + n2-count2[choice2[0]])
            elif len(choice1) > 1 and not len(choice2) > 1:
                return n1-count1[choice1[1]]
            elif not len(choice1) > 1 and len(choice2) > 1:
                return n2-count2[choice2[1]]
            else:
                return min(n1, n2)