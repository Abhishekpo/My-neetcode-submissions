class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS=len(heights)
        COLS=len(heights[0])
        pafset=set()
        altset=set()

        def dfs(r, c, visit, prevheight):

            if(min(r,c)<0 or r==ROWS or c==COLS or (r,c) in visit or 
             heights[r][c] < prevheight):
             return
            visit.add((r,c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
        
        for r in range(ROWS):
            dfs(r, 0, pafset, heights[r][0])
            dfs(r, COLS-1, altset, heights[r][COLS-1])
        for c in range(COLS):
            dfs(0, c, pafset, heights[0][c])
            dfs(ROWS-1,c, altset, heights[ROWS-1][c])
        res=[]
        for r in range(ROWS):
            for c in range(COLS):
                if((r,c) in pafset and (r,c) in altset):
                    res.append([r,c])
        return res
            
           