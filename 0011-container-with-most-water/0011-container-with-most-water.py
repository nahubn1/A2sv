class Solution:
    def maxArea(self, height: List[int]) -> int:
        areas = []
        ptr1 = 0
        ptr2 = len(height) - 1
        
        while ptr1 < ptr2:
            area = (ptr2-ptr1)*min([height[ptr1], height[ptr2]])
            areas.append(area)
            if height[ptr1] > height[ptr2]:
                ptr2 -= 1
            else:
                ptr1 += 1
                
        return max(areas)
        