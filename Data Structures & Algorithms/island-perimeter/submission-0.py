class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        direction=[[1,0],[-1,0],[0,-1],[0,1]]
        visited=set()

        
        def dfs(r, c):
            
            if(r>=row or c>=col or r<0 or c<0 or 
            grid[r][c]==0):
             return 1
            if((r,c) in visited):
                return 0

            visited.add((r,c))
            ans=0
            for dr, dc in direction:
                rn=dr+r 
                cn=dc+c
                if((rn, cn) not in visited):
                    ans +=dfs(rn, cn)

            return ans

        for i in range(row):
            for j in range(col):
                if(grid[i][j]==1):
                   return dfs(i,j)
                    
        return 0
            


                
        
    
        