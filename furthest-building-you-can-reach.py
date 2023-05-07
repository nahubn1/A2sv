class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        height_to_jump = 0
        used_ladder = 0
        heap = []

        i = 1
        while i < len(heights): 
        
            if heights[i] > heights[i-1]:
                diff = heights[i]-heights[i-1]
                height_to_jump += diff

                if ladders:
                    if len(heap) < ladders:
                        heappush(heap, diff)
                        used_ladder += diff
                    else:
                        if diff > heap[0]:
                            used_ladder -= heappop(heap)
                            heappush(heap, diff)
                            used_ladder += diff

            if height_to_jump > bricks + used_ladder:
                return i-1

            i += 1
               
        return i-1