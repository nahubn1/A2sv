class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        def downShift(grid):
            grid.pop()
            grid.appendleft(0)
            return grid

        def upShift(grid):
            grid.popleft()
            grid.append(0)
            return grid
            
        def leftShift(grid):
            for i in range(n):
                grid[i] <<= 1
                grid[i] &= ~(1<<n)
            return grid

        def rightShift(grid):
            for i in range(n):
                grid[i] >>= 1
            return grid
        
        def bitmask(img):
            grid = deque([0]*n)

            for i in range(n):
                for j in range(n):
                    grid[i] |= (img[i][j]<<j) 
            
            return grid
        
        bImg1 = bitmask(img1)
        bImg2 = bitmask(img2)

        que = deque([(bImg1, (0, 0))])
        visited = set([(0, 0)])
        ans = 0
        while que:
            
            img, (r, c) = que.popleft()
            
            if not any(img): continue
            
            overlap = 0
            for i in range(n):
                overlap += (img[i] & bImg2[i]).bit_count()
            
            ans = max(ans, overlap)

            if (r+1, c) not in visited:
                que.append((downShift(img.copy()), (r+1, c)))
                visited.add((r+1, c))
            if (r, c+1) not in visited:
                que.append((rightShift(img.copy()), (r, c+1)))
                visited.add((r, c+1))
            if (r-1, c) not in visited:
                que.append((upShift(img.copy()), (r-1, c)))
                visited.add((r-1, c))
            if (r, c-1) not in visited:
                que.append((leftShift(img.copy()), (r, c-1)))
                visited.add((r, c-1))

        return ans