class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=defaultdict(set)
        cols=defaultdict(set)
        square=defaultdict(set) # we implement it as key value pair where
        # keys will be (r//3 , c//3) this will give us 9 different boxes as
        # we needed

        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                if(board[r][c] in rows[r] 
                 or board[r][c] in cols[c] or 
                 board[r][c] in square[(r//3,c//3)]):
                 return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                square[(r//3, c//3)].add(board[r][c])
        return True