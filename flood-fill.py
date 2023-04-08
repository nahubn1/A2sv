class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        if start_color == color:
            return image

        def dfs(r, c):
            image[r][c] = color 
            for r_step, c_step in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0<=r+r_step <len(image) and 0<=c+c_step <len(image[0]) and  image[r+r_step][c+c_step] == start_color:
                    dfs(r+r_step, c+c_step)

        dfs(sr, sc)
        return image