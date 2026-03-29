class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowhash=defaultdict(set)
        colhash=defaultdict(set)
        squarehash=defaultdict(set)

        for i in range(9):
            for j in range(9):
                if(board[i][j] in rowhash[i] or board[i][j] in colhash[j]
                or board[i][j] in squarehash[(i//3, j//3)]):
                 return False
                if(board[i][j]=="."):
                    continue
                rowhash[i].add(board[i][j])
                colhash[j].add(board[i][j])
                squarehash[(i//3, j//3)].add(board[i][j])

        return True

                 
                
