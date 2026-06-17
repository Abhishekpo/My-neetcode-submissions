class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #[["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
        # word = "ABCESEEEFS"

        # [["C","A","A"],["A","A","A"],["B","C","D"]]
        # words = "AAB"

        R = len(board)
        C = len(board[0])

        visited =set()

        def dfs(r, c, i):


            if len(word) == i:
                return True

            if r >= R or c >= C or r < 0 or c < 0 or (r,c) in visited or board[r][c] != word[i]:
                return False
            
            visited.add((r,c))
            
            
            res = dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)
            visited.remove((r,c)) # we need to remove the path if that path is visited and failed
            # because another path from another direction might use char form that path or they might 
            # corss their paths
            return res 
        
        for i in range(R):
            for j in range(C):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True
        return False
