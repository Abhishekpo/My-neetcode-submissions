class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        row, col = len(board), len(board[0])
        myset=set()

        
         
        def helper(r, c, i):

         if(min(r, c)< 0 or r>=row or c>=col or (r,c) in myset 
         or board[r][c] != word[i] ):
           return False

         if(i==len(word)-1):
            return True
        
         myset.add((r,c))

         res= helper(r+1,c,i+1) or helper(r-1,c,i+1) or helper(r,c+1,i+1) or helper(r,c-1,i+1)

         myset.remove((r,c))
         return res

        for i in range(row):
            for j in range(col):
                if helper(i,j,0):
                    return True
        
        return False

          
          
