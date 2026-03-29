class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dfs(i):
            if(i==1 or i ==0):
                return 1
            if(i<0):
                return 0
            left=dfs(i-1)
            right=dfs(i-2)
            return left+right
        return dfs(n)
        