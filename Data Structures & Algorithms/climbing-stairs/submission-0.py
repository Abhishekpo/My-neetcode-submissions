class Solution:
    def climbStairs(self, n: int) -> int:
        # dfs 
        res=0
        def dfs(start):
            if start==n:
                return 1
            if start >n:
                return 0
            res= dfs(start+1) + dfs(start+2)
            return res
        return dfs(0)