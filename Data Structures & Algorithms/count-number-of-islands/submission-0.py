class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

     row, col =len(grid), len(grid[0])
     count=0
     myset=set()

     def dfs(r,c,i):
        if(min(r,c)<0 or r>=row or c >=col or grid[r][c] =="0" or (r,c) in myset):
            return 
        myset.add((r,c))
        dfs(r+1,c,i+1) or dfs(r-1, c,i+1) or dfs(r, c+1,i+1) or dfs(r,c-1,i+1)

        return

     for i in range(row):
         for j in range(col):
             if (i, j) in myset or grid[i][j]=="0":
                continue
             count +=1
             dfs(i,j,0)
     return count