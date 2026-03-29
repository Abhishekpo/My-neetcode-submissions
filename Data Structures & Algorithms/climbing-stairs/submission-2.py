class Solution:
    def climbStairs(self, n: int) -> int:
        
        res=0
        climb1=0
        climb2=0
        def dfs(i):
         if i==n:
            return 1
         if i>n:
            return 0
         climb1=dfs(i+1)
         climb2=dfs(i+2)
         res=climb1+climb2
         return res
        
        res=dfs(0)
        return res
         