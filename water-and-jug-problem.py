class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        lo, hi = 0, jug1Capacity+jug2Capacity
        candidates = [jug1Capacity, jug2Capacity, -jug1Capacity, -jug2Capacity]

        que = deque([0])
        visited = set([0])

        while que:

            num = que.popleft()
            if num == targetCapacity:
                return True

            for cand in candidates:
                if 0 <= num+cand <= jug1Capacity+jug2Capacity and num+cand not in visited:
                    que.append(num+cand)
                    visited.add(num+cand)

        return False