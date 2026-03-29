class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row=len(grid)
        col=len(grid[0])
        visit=set()
        length=0

        def dfs(r, c, visit):
            
            if(min(r, c)<0 or r>=row or c >=col or grid[r][c] !="1" or (r, c) in visit):
                return 
            visit.add((r,c))

            dfs(r+1, c, visit)
            dfs(r-1, c, visit)
            dfs(r, c+1, visit)
            dfs(r, c-1, visit)
            return
        
        for r in range(row):
            for c in range(col):
                if(grid[r][c]=="0" or (r, c) in visit):
                    continue
                else:
                 dfs(r, c, visit)
                 length +=1

        return length
                

