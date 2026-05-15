class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        

    

        # bFS
        R = len(grid)
        C = len(grid[0])
        queue = deque()
        myset=set()
        for i in range(R):
            istrue=False
            for j in range(C):
                if grid[i][j]==1:
                    queue.append((i,j))
                    myset.add((i,j))
                    istrue=True
            if istrue:
                break

        
        directions=[(0,1),(0,-1), (1, 0), (-1,0)]
        res=0
        while queue:
            rowpop, colpop = queue.popleft()
            for r, c in directions:
                newrow = rowpop + r
                newcol = colpop + c

                if newrow >= R or newrow < 0 or newcol < 0 or newcol >= C or grid[newrow][newcol] == 0:
                    res +=1
                    continue

                if (newrow, newcol) in myset:
                    continue
                
                queue.append((newrow, newcol))
                myset.add((newrow, newcol))

        return res
            