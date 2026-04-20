class Solution:
    def tribonacci(self, n: int) -> int:
        mem=[-1]*(n+1)

        def dfs(i):
            if i == 0:
                return 0

            if i <=2:
                return 1
            
            if mem[i] != -1:
                return mem[i]

            mem[i]=dfs(i-1)+dfs(i-2)+dfs(i-3)
            return mem[i]
        return dfs(n)