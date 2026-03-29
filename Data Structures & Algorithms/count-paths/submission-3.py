class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*n for i in range(m)]
        dp[m-1][n-1]=1
        def dfs(r, c):

            if(r==m or c==n):
                return 0
            if(dp[r][c]):
                return dp[r][c]
        
            right=dfs(r,c+1)
            down=dfs(r+1, c)
           
            dp[r][c]=right+down
            return dp[r][c]
        return dfs(0,0)