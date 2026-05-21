class Solution:
    def solve(self, board: List[List[str]]) -> None:

        R = len(board)
        C = len(board[0])
        directions= [(1, 0), (0,1), (-1,0), (0,-1)]

        visited=set()
        queue = deque()

        for i in range(R):
            for j in range(C):
                if (i == 0 or j == 0 or i == R-1 or j == C-1) and board[i][j] == "O":
                 queue.append((i,j))
                 visited.add((i,j))

        
        while queue:

            popr, popc = queue.popleft()

            for dr, dc in directions:
                drn, dcn = popr + dr, popc + dc
                
                if drn < 0 or dcn < 0 or drn >= R or dcn >= C or (drn, dcn) in visited or board[drn][dcn] != "O":
                    continue
                
                visited.add((drn, dcn))
                queue.append((drn, dcn))
        
        for i in range(R):
            for j in range(C):
                if (i, j) not in visited and board[i][j] == 'O':
                    board[i][j] = "X"

        

            

            
        