class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        if n < 3 or m < 3:
            return 0

        magic_box = 0
        for i in range(n-2):
            for j in range(m-2):
                
                r_sum = [0]*3
                c_sum = [0]*3
                d1_sum = d2_sum = 0 
                
                nums = set()
                for r in range(3):
                    for c in range(3):
                        nums.add(grid[i+r][j+c])
                        r_sum[r] += grid[i+r][j+c]
                        c_sum[c] += grid[i+r][j+c]
                        
                        if r+c == 2:
                            d1_sum += grid[i+r][j+c]

                        if r-c == 0:
                            d2_sum += grid[i+r][j+c]
                # print(i, j)
                # print(r_sum[0], r_sum[1], r_sum[2], c_sum[0], c_sum[1], c_sum[2], d1_sum, d2_sum)
                # print(nums)
                # print(len(nums) == 9 and min(nums) == 1 and max(nums) == 9)
                if len(nums) == 9 and min(nums) == 1 and max(nums) == 9:
                    if r_sum[0]==r_sum[1]==r_sum[2]==c_sum[0]==c_sum[1]==c_sum[2]==d1_sum==d2_sum:
                        magic_box += 1
        
        return magic_box
                