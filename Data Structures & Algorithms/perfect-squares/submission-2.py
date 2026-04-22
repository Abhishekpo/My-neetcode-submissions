class Solution:
    def numSquares(self, n: int) -> int:
        
        dp=[float('inf')]*(n+1)
        dp[0]=0
        
        for rem in range(1, n+1):
            i=1
            while i*i <=rem:
                dp[rem]=min(dp[rem], 1+dp[rem-i*i])
                i +=1
        return dp[n]