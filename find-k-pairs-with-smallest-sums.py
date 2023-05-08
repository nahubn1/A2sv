class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)

        heap = []
        for i in range(len(nums1)):
            heap.append((nums1[i]+nums2[0], i, 0))
        
        heapify(heap)

        pairs = []
        while len(pairs) < k and heap:
            
            val, i1, i2 = heappop(heap)

            pairs.append((nums1[i1], nums2[i2]))

            i2 += 1
            if i2 < n:
                val += (nums2[i2] - nums2[i2-1])
                heappush(heap, (val, i1, i2))
        
        return pairs