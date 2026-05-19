class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        R = len(grid)
        C = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        fresh = 0

        queue = deque()
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    queue.append((i,j))
                   
                if grid[i][j] == 1:
                    fresh += 1
                    
        ans = 0
        while queue and fresh > 0:

            for i in range(len(queue)):
                popr, popc = queue.popleft()

                for dr, dc in directions: 
                 drn, dcn = dr + popr, dc + popc

                 if drn < 0 or drn >= R or dcn < 0 or dcn >= C or grid[drn][dcn] == 0 or grid[drn][dcn] == 2:
                     continue

                 fresh -= 1
                 grid[drn][dcn] = 2
                 queue.append((drn, dcn))

            ans  += 1

        return ans if fresh == 0 else -1 # this means if there is no fresh fruit left
        # then return the count else dont return the unsuccessful count.
