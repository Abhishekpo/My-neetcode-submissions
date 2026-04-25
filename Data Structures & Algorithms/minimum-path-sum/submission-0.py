class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        col = len(grid[0])
        mem = {(row-1, col-1): grid[row-1][col-1]}

        def dfs(i, j): # the minimum path to go frim here 

            if (i,j) in mem:
                return mem[(i,j)]

            if i==row or j==col:
                return float("inf")
            
            res = grid[i][j]+ min( dfs(i, j+1), dfs(i+1, j))
            mem[(i,j)]=res
            return res

        return dfs(0,0)

