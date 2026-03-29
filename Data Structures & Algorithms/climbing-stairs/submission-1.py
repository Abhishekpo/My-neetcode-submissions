class Solution:
    def climbStairs(self, n: int) -> int:
        # dfs 
        res=0
        cache={}
        def dfs(start):
            if start==n:
                return 1
            if start >n:
                return 0
            if start in cache:
                return cache[start]
            cache[start]= dfs(start+1) + dfs(start+2)
            return cache[start]
        return dfs(0)