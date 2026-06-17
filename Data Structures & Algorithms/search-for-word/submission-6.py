class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        R = len(board)
        C = len(board[0])

        def dfs(r, c, i, visited):


            if len(word) == i:
                return True

            if r >= R or c >= C or r < 0 or c < 0 or (r,c) in visited or board[r][c] != word[i]:
                return False
            
            visited.add((r,c))
            
            
            res = dfs(r+1, c, i+1, visited) or dfs(r-1, c, i+1, visited) or dfs(r, c+1, i+1, visited) or dfs(r, c-1, i+1, visited)
            visited.remove((r,c)) # we need to remove the path if that path is visited and failed
            # because another path from another direction might use char form that path
            return res 
        
        for i in range(R):
            for j in range(C):
                if board[i][j] == word[0]:
                    if dfs(i,j,0, set()):
                        return True
        return False
