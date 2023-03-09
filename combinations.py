class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def collect(start, arr):
            if len(arr) == k:
                ans.append(arr)
                return

            for i in range(start, n+1):
                collect(i+1, arr+[i])

        collect(1, [])

        return ans