class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = 0
        point_1 = 0
        point_2 = 0

        for i, val in enumerate(values):
            point_2 = val-i
            ans = max(ans, point_1 + point_2)
            point_1 = max(point_1, val+i)

        return ans