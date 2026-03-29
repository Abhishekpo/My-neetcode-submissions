class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dfs(i):
            if(i==n):
                return 1
            if(i>n):
                return 0
            left=dfs(i+1)
            right=dfs(i+2)
            return left+right
        return dfs(0)
        