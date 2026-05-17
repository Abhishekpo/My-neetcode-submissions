class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        R = len(grid)
        C = len(grid[0])

        visited = set()
        def dfs(r, c):

            if r < 0 or r >= R or c < 0 or c >= C or (r, c) in visited or grid[r][c] == 0:
                return 0
            
            visited.add((r, c))

            ans = 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

            return ans
        
        maxval = 0
        for i in range(R):
            for j in range(C):
                if (i, j) not in visited and grid[i][j] == 1:
                    maxval = max(maxval, dfs(i, j))

        return maxval
                    
        