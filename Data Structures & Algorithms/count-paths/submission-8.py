class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[1]*n # this is space optimized version
        
        
        for i in range(m-1):
            temp=[0]*n
            temp[n-1]=1
            for j in range(n-2, -1, -1):
                temp[j]=dp[j]+temp[j+1]
            dp=temp
            

        return dp[0]