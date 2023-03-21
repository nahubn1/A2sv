class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        que = deque([0])
        preSum = [0]
        minWin = inf
        for i in range(len(nums)):
            preSum.append(preSum[-1]+nums[i])
            
            while que and preSum[-1] - preSum[que[0]] >= k:
                minWin = min(minWin, i - que[0] + 1)
                que.popleft()
            
            while que and preSum[que[-1]] >= preSum[-1]:
                que.pop()
            que.append(i+1)

        return minWin if minWin < inf else -1