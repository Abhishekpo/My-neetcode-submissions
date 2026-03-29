class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row=len(grid)
        cols=len(grid[0])

        my_set=set()

        def dfs(r, c):

            if(r<0 or c<0 or r>=row or c>=cols or grid[r][c]!="1" or (r,c) in my_set):
                return False
            
            my_set.add((r,c))
            res=(dfs(r+1, c) or dfs(r-1, c) or dfs(r, c+1) or dfs(r, c-1))

            return False
        total=0
        for r in range(row):
            for c in range(cols):
                if grid[r][c] =="1" and (r,c) not in my_set:
                 total +=1
                 dfs(r,c)
                   
        return total