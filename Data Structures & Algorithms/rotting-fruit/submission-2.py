class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        R = len(grid)
        C = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        queue = deque()
        visited= set()
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    visited.add((i,j))
        ans = 0
        while queue:

            for i in range(len(queue)):
                popr, popc = queue.popleft()

                for dr, dc in directions: 
                 drn, dcn = dr + popr, dc + popc

                 if drn < 0 or drn >= R or dcn < 0 or dcn >= C or grid[drn][dcn] == 0 or (drn, dcn) in visited:
                     continue
                
                 visited.add((drn, dcn))
                 queue.append((drn, dcn))

            if queue: # needs to check this because last elements in the queue does nothing and we get off by 1 error
             ans += 1

        for i in range(R):
            for j in range(C):
                if (i, j) not in  visited and grid[i][j]==1:
                    return -1
        return ans
