class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=2: # we have to do this because it its 1 then below will be out of bound
            return n

        dp=[0]*(n+1)
        dp[1]=1
        dp[2]=2  # this one
        for i in range(3, n+1):
            dp[i]=dp[i-1]+dp[i-2]

        return dp[n]