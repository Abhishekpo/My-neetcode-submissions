class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row=len(grid)
        col=len(grid[0])
        visit=set()
        length=0

        
        def bfs(r, c, visit):
            queue=deque()
            visit.add((r,c))
            queue.append((r,c))
            
            while queue:
               direction=[[1,0],[-1,0],[0,1],[0,-1]]
               rd, cd=queue.popleft()

               for  dr, dc in direction:
                nr, nc=dr+rd, cd+dc
                if(min(nr, nc)<0 or nr>=row or nc>=col or grid[nr][nc]!="1" or (nr,nc) in visit ):
                    continue
                queue.append((nr,nc))
                visit.add((nr,nc))

        for r in range(row):
            for c in range(col):
                if(grid[r][c]=="1" and (r,c) not in visit):
                    bfs(r, c, visit)
                    length +=1
                

        return length
                    

            


         


