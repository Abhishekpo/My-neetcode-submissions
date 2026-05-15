class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
     R=len(grid)
     C=len(grid[0])
     myset=set()

    

     def dfs(row, col):
        if row >= R or row < 0 or col >= C or col < 0 or grid[row][col]==0:
            return 1

        if (row, col) in myset:
            return 0

        myset.add((row, col))
        
        return dfs(row+1, col) + dfs(row, col+1) + dfs(row-1, col) + dfs(row, col-1)

     for i in range(R):
        for j in range(C):
            if grid[i][j]==1:
               return dfs(i, j)