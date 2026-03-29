class Solution:
    def climbStairs(self, n: int) -> int:
        mem=[0 for i in range(n+1)]
        def dfs(i):
            if(i==1 or i ==0):
                return 1
            if(i<0):
                return 0
            if(mem[i]):
                return mem[i]
            left=dfs(i-1)
            right=dfs(i-2)
            mem[i]=left+right
            return mem[i]
        return dfs(n)
        