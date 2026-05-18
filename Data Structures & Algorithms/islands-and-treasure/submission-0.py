class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        R = len(grid)
        C = len(grid[0])

        directions =[(0,1),(1,0),(-1, 0), (0, -1)]

        queue = deque()
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    queue.append((i, j))
        visited = set()
        while queue:

            r , c = queue.popleft()

            for dr, dc in directions:
                newr, newc = r + dr , c + dc
                if newr < 0 or newc < 0 or newr >= R or newc >= C or grid[newr][newc] == -1 or (newr, newc) in visited:
                    continue
                
                if grid[newr][newc] != 2147483647:
                    continue

                visited.add((newr, newc))
                queue.append((newr, newc))
                grid[newr][newc] = 1 + grid[r][c]
            
        

                
                

