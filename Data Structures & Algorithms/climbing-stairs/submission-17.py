class Solution:
    def climbStairs(self, n: int) -> int:
        res=[0]*(n+1)
        def dfs(i):

            if(i>n):
             return 0

            if(i==n):
                res[i]=1
                return res[i]

            if(res[i] !=0):
                return res[i]
            
            res[i]=dfs(i+1)+dfs(i+2)
            return res[i]
        dfs(0)
        return res[0]