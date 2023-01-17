class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for start in range(len(names)):
            max_idx = start
            for i in range(start, len(names)):
                if heights[max_idx] < heights[i]:
                    max_idx = i
            
            names[start], names[max_idx] = names[max_idx], names[start]
            heights[start], heights[max_idx] = heights[max_idx], heights[start]
            
        return names